# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20170916_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activityreport',
            options={'ordering': ['-created_on', '-resolved'], 'verbose_name': 'Activity Report', 'verbose_name_plural': 'Activity Reports'},
        ),
        migrations.AlterField(
            model_name='activityreport',
            name='content',
            field=models.TextField(help_text=b"A description of the activity you're reporting. If this is a life-threatening emergency, please notify emergency services.", verbose_name=b'Report'),
        ),
    ]