# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_merge_20171003_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitybond',
            name='fitch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='moody',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securitybond',
            name='s_and_p',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='first_notice_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='maturity_date',
            field=models.DateTimeField(),
        ),
    ]
