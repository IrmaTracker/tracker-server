# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from callapp.models import  Post, Emergency, HelpLine, Need

# Register your models here.


class EmergencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'place', 'status', 'time', 'solved']
    list_filter = ['solved']


class HelpLineAdmin(admin.ModelAdmin):
    list_display = ['title', 'place', 'created_on']


class NeedAdmin(admin.ModelAdmin):
    list_display = ['name', 'time', 'contact', 'location', 'solved']


admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(HelpLine, HelpLineAdmin)
admin.site.register(Need, NeedAdmin)
admin.site.register([Post])
