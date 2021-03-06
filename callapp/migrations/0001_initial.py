# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Status')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Link')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Name')),
                ('time', models.CharField(blank=True, max_length=75, null=True, verbose_name=b'Time')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Place')),
                ('solved', models.BooleanField(default=False, verbose_name=b'Solved')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'emergencies',
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergencies',
            },
        ),
        migrations.CreateModel(
            name='HelpLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Place')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name=b'Content')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
            ],
            options={
                'db_table': 'help_lines',
            },
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, help_text=b'Latitude', max_digits=9, null=True, verbose_name=b'Lat')),
                ('long', models.DecimalField(blank=True, decimal_places=6, help_text=b'Longitude', max_digits=9, null=True, verbose_name=b'Long')),
                ('need_id', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Need id')),
                ('need', models.TextField(blank=True, null=True, verbose_name=b'Need')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Link')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Name')),
                ('time', models.CharField(blank=True, max_length=75, null=True, verbose_name=b'Time')),
                ('contact', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Contact')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Location')),
                ('solved', models.BooleanField(default=False, verbose_name=b'Solved')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
            ],
            options={
                'db_table': 'needs',
                'verbose_name': 'Need',
                'verbose_name_plural': 'Needs',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Name')),
                ('link', models.URLField(blank=True, null=True, verbose_name=b'Link')),
                ('time', models.CharField(blank=True, max_length=75, null=True, verbose_name=b'Time')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Status')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'posts',
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
