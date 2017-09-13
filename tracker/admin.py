# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tracker.models import Person, Area, EmergencyRequest, SupplySharing, SupplyRequest, Supply
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PersonResource(resources.ModelResource):
    """
    A Resource for Django Import Export
    """
    class Meta:
        model = Person
        import_id_fields = ('name',)
        fields = ('name', 'district', 'phonenumber', 'address', 'safe', 'extra_info')


class CustomPersonAdmin(ImportExportModelAdmin):
    list_filter = ('safe', 'area__name', 'notified')
    list_display = ('name', 'district', 'address', 'area', 'safe')
    search_fields = ('name', 'phonenumber', 'district', 'address')
    resource_class = PersonResource


class CustomEmergencyRequestAdmin(ImportExportModelAdmin):
    list_filter = ('resolved',)
    list_display = ('full_name', 'address', 'district', 'resolved')
    search_fields = ('full_name', 'address', 'district')


class CustomSupplyAdmin(ImportExportModelAdmin):
    list_filter = ('resolved',)
    list_display = ('full_name', 'address', 'district', 'resolved')
    search_fields = ('full_name', 'address', 'district')


# Register models for Admin
admin.site.register(Person, CustomPersonAdmin)
admin.site.register(EmergencyRequest, CustomEmergencyRequestAdmin)
admin.site.register(SupplySharing, CustomSupplyAdmin)
admin.site.register(SupplyRequest, CustomSupplyAdmin)
admin.site.register([Area, Supply])

# portal overrides
admin.site.site_title = "Tracker Admin"
admin.site.index_title = "Person Tracker"
admin.site.site_header = "Tracker Admin"