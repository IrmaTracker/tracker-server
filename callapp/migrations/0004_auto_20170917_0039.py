# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callapp', '0003_remove_need_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Link'),
        ),
    ]