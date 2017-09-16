# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_helpline_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, help_text=b'Latitude', max_digits=9, null=True, verbose_name=b'Lat')),
                ('long', models.DecimalField(blank=True, decimal_places=6, help_text=b'Longitude', max_digits=9, null=True, verbose_name=b'Long')),
                ('status', models.CharField(max_length=255, verbose_name=b'Status')),
                ('link', models.CharField(max_length=255, verbose_name=b'Link')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('time', models.CharField(max_length=75, verbose_name=b'Time')),
                ('solved', models.BooleanField(default=False, verbose_name=b'Solved')),
            ],
            options={
                'db_table': 'emergencies',
            },
        ),
    ]