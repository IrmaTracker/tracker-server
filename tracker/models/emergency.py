from django.db import models
from tracker.models import AbstractRequestBase


class Emergency(AbstractRequestBase):
    """
    CallApp Table
    """

    status = models.CharField("Status", max_length=255)
    link = models.CharField("Link", max_length=255)
    name = models.CharField("Name", max_length=255)
    time = models.CharField("Time", max_length=75)
    solved = models.BooleanField("Solved", default=False)

    class Meta:
        db_table = "emergencies"