# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='need',
            options={'ordering': ['created_on', '-solved'], 'verbose_name': 'Need', 'verbose_name_plural': 'Needs'},
        ),
    ]