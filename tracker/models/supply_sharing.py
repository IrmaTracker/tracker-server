from django.db import models
from tracker.constants import SHAREABLE_SUPPLIES_TF, PICKUP_INSTRUCTIONS
from tracker.models import AbstractRequestBase


class SupplySharing(AbstractRequestBase):
    shareable_supplies = models.TextField("Shareable Supplies", null=True, blank=True, help_text=SHAREABLE_SUPPLIES_TF)
    pickup_instructions = models.TextField("Pickup Instructions", null=True, blank=True, help_text=PICKUP_INSTRUCTIONS)

    class Meta:
        db_table = "supply_sharing"
        verbose_name = "Supply Sharing"
        verbose_name_plural = "Supply Sharing"

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name
