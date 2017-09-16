from django.db import models
from tracker.models import AbstractBaseLocation


class Emergency(AbstractBaseLocation):
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

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name