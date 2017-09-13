# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_auto_20170909_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name=b'Full name')),
                ('address', models.CharField(db_index=True, help_text=b'Street and number', max_length=255, verbose_name=b'Address')),
                ('district', models.CharField(db_index=True, help_text=b'I.e. Cupecoy, Cayhill, etc.,', max_length=128, verbose_name=b'District')),
                ('contact_numbers', models.CharField(blank=True, max_length=128, null=True, verbose_name=b'Contact Numbers')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
                ('has_24_hours', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], db_index=True, default=1, verbose_name=b'Will you survive the next 24 hours?')),
                ('has_injuries', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], db_index=True, default=0, verbose_name=b'Injuries')),
                ('has_rain_shelter', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], db_index=True, default=0, help_text=b'Does your location have shelter from the rain?', verbose_name=b'Rain shelter')),
                ('has_shareable_supplies', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], db_index=True, default=0, help_text=b'Do you have supplies you can share?', verbose_name=b'Shareable supplies')),
                ('has_lod_situation', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], db_index=True, default=0, help_text=b'Are any of you in a life or death situation?', verbose_name=b'Life or death situation')),
                ('shareable_supplies', models.TextField(blank=True, help_text=b'Specify the type of supplies and their quantities', null=True, verbose_name=b'Shareable Supplies')),
                ('additional_persons', models.TextField(blank=True, help_text=b'Who else is at your location?', null=True, verbose_name=b'Additional Persons')),
                ('days_of_food', models.IntegerField(choices=[(0, b'None'), (1, b'Enough for 1 day'), (2, b'Enough for 2 days'), (3, b'Enough for more than 3 days')], help_text=b'How many days of food supplies do you have?', verbose_name=b'Days of food')),
                ('days_of_water', models.IntegerField(choices=[(0, b'None'), (1, b'Enough for 1 day'), (2, b'Enough for 2 days'), (3, b'Enough for more than 3 days')], help_text=b'How many days of food supplies do you have?', verbose_name=b'Days of drinking water')),
                ('requires_medical_supplies', models.IntegerField(choices=[(0, b'No'), (1, b'Yes')], default=0, help_text=b'Does anyone need immediate medical supplies?', verbose_name=b'Need immediate medical supplies')),
                ('medical_supplies', models.TextField(blank=True, help_text=b"If you answered 'Yes' to medical supplies, please specify the supplies you need.", null=True, verbose_name=b'Medical supplies')),
                ('type_of_injuries', models.TextField(blank=True, help_text=b"If you answered 'Yes' to injuries, please specify the injuries.", null=True, verbose_name=b'Type of injuries')),
                ('request', models.TextField(help_text=b'In short, can you describe your emergency and/or request', verbose_name=b'Request')),
                ('urgency_ranking', models.IntegerField(default=5, verbose_name=b'Urgency ranking')),
            ],
            options={
                'db_table': 'emergency_requests',
                'verbose_name': 'Emergency Request',
                'verbose_name_plural': 'Emergency Requests',
            },
        ),
        migrations.CreateModel(
            name='SupplyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name=b'Full name')),
                ('address', models.CharField(db_index=True, help_text=b'Street and number', max_length=255, verbose_name=b'Address')),
                ('district', models.CharField(db_index=True, help_text=b'I.e. Cupecoy, Cayhill, etc.,', max_length=128, verbose_name=b'District')),
                ('contact_numbers', models.CharField(blank=True, max_length=128, null=True, verbose_name=b'Contact Numbers')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created on')),
                ('additional_persons', models.TextField(blank=True, help_text=b'Who else is at your location?', null=True, verbose_name=b'Additional Persons')),
                ('shareable_supplies', models.TextField(blank=True, help_text=b'Specify the type of supplies and their quantities', null=True, verbose_name=b'Shareable Supplies')),
            ],
            options={
                'db_table': 'supply_requests',
                'verbose_name': 'Supply Request',
                'verbose_name_plural': 'Supply Requests',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='safe_email_send',
        ),
        migrations.AlterUniqueTogether(
            name='emergencyrequest',
            unique_together=set([('address', 'district')]),
        ),
    ]
