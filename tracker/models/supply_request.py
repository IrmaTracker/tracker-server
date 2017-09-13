from django.db import models
from tracker.constants import NEEDED_SUPPLIES_TF, PICKUP_INSTRUCTIONS, SUPPLY_REQUEST_QUANTITY
from tracker.models import AbstractRequestBase


class SupplyRequest(AbstractRequestBase):
    supplies = models.ManyToManyField('Supply', db_index=True, help_text=NEEDED_SUPPLIES_TF)
    quantity = models.IntegerField("Amount of people", default=1, help_text=SUPPLY_REQUEST_QUANTITY)
    dropoff_instructions = models.TextField("Dropoff Instructions", null=True, blank=True, help_text=PICKUP_INSTRUCTIONS)

    class Meta:
        ordering = ['created_on', '-resolved']
        db_table = "supply_requests"
        verbose_name = "Supply Request"
        verbose_name_plural = "Supply Requests"

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name