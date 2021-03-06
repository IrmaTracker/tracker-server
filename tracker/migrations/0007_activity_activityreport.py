# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20170916_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name=b'Activity name')),
                ('description', models.TextField(blank=True, null=True, verbose_name=b'Activity description')),
            ],
            options={
                'db_table': 'activities',
            },
        ),
        migrations.CreateModel(
            name='ActivityReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name=b'Address')),
                ('content', models.TextField(help_text=b'If this is a life-threatening emergency, please notify emergency services.', verbose_name=b'Report')),
                ('resolved', models.BooleanField(db_index=True, default=False, verbose_name=b'Resolved')),
                ('district', models.CharField(db_index=True, max_length=255, verbose_name=b'District')),
                ('reporter_name', models.CharField(max_length=255, verbose_name=b'Reported name')),
                ('reporter_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'Reporter email')),
                ('reporter_number', models.CharField(blank=True, max_length=75, null=True, verbose_name=b'Reporter number')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name=b'Updated on')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Area')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Activity')),
            ],
            options={
                'ordering': ['created_on', '-resolved'],
                'db_table': 'activity_reports',
            },
        ),
    ]
