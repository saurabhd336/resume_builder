# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_resume_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume_file',
            field=models.FileField(default='', upload_to=b''),
        ),
    ]