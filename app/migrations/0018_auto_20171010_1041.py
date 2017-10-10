# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitybond',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AlterField(
            model_name='securityfutures',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AlterField(
            model_name='securityoption',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AlterField(
            model_name='securityshare',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
    ]