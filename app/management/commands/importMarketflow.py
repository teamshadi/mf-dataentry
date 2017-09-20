import logging
from ._mfManager import MfManager
from ...models import Currency, Nationality


# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
from django.core.management.base import BaseCommand

import progressbar
logger = logging.getLogger('MF data entry')


class Command(BaseCommand):
  help = """Usage:
         python manage.py importMarketflow --help
         python manage.py importMarketflow --debug
         """

  def add_arguments(self, parser):
    parser.add_argument('--debug',   action='store_true', dest='debug',                   help='show higher verbosity',                           default=False)
    parser.add_argument('--host',    action='store',      dest='host',     required=True, help='ms sql server for marketflow: host IP or name')
    parser.add_argument('--port',    action='store',      dest='port',     required=True, help='ms sql server for marketflow: port number')
    parser.add_argument('--user',    action='store',      dest='user',     required=True, help='ms sql server for marketflow: username')
    parser.add_argument('--password',action='store',      dest='password', required=True, help='ms sql server for marketflow: password')
    parser.add_argument('--db',      action='store',      dest='db',       required=True, help='ms sql server for marketflow: database name')
    parser.add_argument('--origin',  action='store',      dest='origin',   required=True, help='Name of origin: Lebanon / Dubai')

  def _handle_core(self, total, listGenerator, keyField, nameField, model):
    
      logger.debug("(%s): Django import %s: %s"%(self.origin, model.__name__, total))
      if self.debug:
        counter = 0
        progress = progressbar.ProgressBar(maxval=total).start()

      for rowMf in listGenerator:
        if self.debug:
          counter+=1
          if counter % 100 == 0:
            # logger.debug("%s / %s"%(counter,total))
            progress.update(counter)
  
        # get/create currency/nationality/etc
        defaults = self._get_defaults(rowMf[keyField])
        #print(rowMf[nameField], defaults)
        rowDj, created = model.objects.update_or_create(
          name = rowMf[nameField],
          defaults = defaults
        )

        if created:
            logger.debug("Created %s: %s"% (model.__name__, rowDj))

      if self.debug:
        progress.finish()

  def _get_defaults(self, value):
    """
    returns {'code_leb': 'bla'} if self.source='MF Lebanon'
    returns {'code_dub': 'bla'} if self.source='MF Dubai'
    """
    map_code = {'MF Lebanon': 'code_leb', 'MF Dubai': 'code_dub'}
    defaults = {value: map_code[self.origin]}
    defaults = {v:k for k,v in defaults.items()}
    return defaults
 
  def _handle_currency(self, mfMan):
      total = mfMan.currenciesCount()
      listGenerator =  mfMan.currenciesList()
      self._handle_core(total, listGenerator, 'DEV_COD', 'DEV_SYM_LGE1', Currency)


  def _handle_nationality(self, mfMan):
      total = mfMan.nationalitiesCount()
      listGenerator =  mfMan.nationalitiesList()
      self._handle_core(total, listGenerator, 'NAT_COD', 'NAT_LIB_LGE1', Nationality)


  def handle(self, *args, **options):
    h1 = logging.StreamHandler(stream=self.stderr)
    logger.addHandler(h1)
    if options['debug']:
      logger.setLevel(logging.DEBUG)

    if options['origin'] not in ('MF Lebanon', 'MF Dubai'):
      raise Exception("Invalid origin found. Please use: 'MF Lebanon' or 'MF Dubai'")

    self.debug = options['debug']
    self.origin = options['origin']

    with MfManager(host=options['host'], port=options['port'], user=options['user'], password=options['password'], db=options['db']) as mfMan:
      self._handle_currency(mfMan)
      self._handle_nationality(mfMan)
