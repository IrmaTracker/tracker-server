# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0028_auto_20170912_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergencyrequest',
            options={'ordering': ['urgency_ranking', 'resolved'], 'verbose_name': 'Emergency Request', 'verbose_name_plural': 'Emergency Requests'},
        ),
        migrations.AlterIndexTogether(
            name='emergencyrequest',
            index_together=set([('urgency_ranking', 'resolved')]),
        ),
    ]
