# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170920_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securitybond',
            old_name='multiplier_fFor_online_prices',
            new_name='multiplier_for_online_prices',
        ),
        migrations.RenameField(
            model_name='securityfutures',
            old_name='multiplier_fFor_online_prices',
            new_name='multiplier_for_online_prices',
        ),
        migrations.RenameField(
            model_name='securityoption',
            old_name='multiplier_fFor_online_prices',
            new_name='multiplier_for_online_prices',
        ),
        migrations.RenameField(
            model_name='securityshare',
            old_name='multiplier_fFor_online_prices',
            new_name='multiplier_for_online_prices',
        ),
    ]
