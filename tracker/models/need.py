from django.db import models
from tracker.models import AbstractBaseLocation


class Need(AbstractBaseLocation):
    """
    CallApp Table
    """

    need_id = models.CharField()
    need = models.CharField("Status", max_length=255)
    link = models.CharField("Link", max_length=255)
    name = models.CharField("Name", max_length=255)
    time = models.CharField("Time", max_length=75)
    contact = models.CharField("Contact", max_length=255)
    location = models.CharField("Location", max_length=255)

    class Meta:
        db_table = "needs"