from django.db import models


class AbstractRequestBase(models.Model):
    full_name = models.CharField("Full name", max_length=128)
    address = models.CharField("Your Address", help_text="Street and number", db_index=True, max_length=255)
    district = models.CharField("District", help_text="I.e. Cupecoy, Cayhill, etc.,", db_index=True, max_length=128)
    contact_numbers = models.CharField("Contact Numbers", max_length=128, null=True, blank=True)
    created_on = models.DateTimeField("Created on", editable=False, auto_now_add=True)
    resolved = models.BooleanField("Request Resolved", default=False, db_index=True)

    # CallApp Specific Columns
    lat = models.DecimalField("Lat", max_digits=9, decimal_places=6, help_text="Latitude", blank=True, null=True)
    long = models.DecimalField("Long", max_digits=9, decimal_places=6, help_text="Longitude", blank=True, null=True)
    time = models.CharField("Time", max_length=75, null=True, blank=True)
    contact = models.CharField("Contact", max_length=128, null=True, blank=True)
    request = models.TextField("Request", null=True, blank=True)

    class Meta:
        abstract = True