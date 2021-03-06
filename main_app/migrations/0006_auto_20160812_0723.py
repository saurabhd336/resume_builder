# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20160812_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='dob',
            field=models.DateField(default=datetime.datetime(2016, 8, 12, 7, 23, 10, 908388)),
        ),
        migrations.AddField(
            model_name='resume',
            name='email_id',
            field=models.EmailField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='resume',
            name='gender',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='resume',
            name='nationality',
            field=models.CharField(default='/', max_length=2000),
        ),
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
