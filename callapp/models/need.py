from django.db import models
from tracker.models import AbstractBaseLocation


class Need(AbstractBaseLocation):
    """
    CallApp Table
    """

    need_id = models.CharField("Need id", max_length=255, null=True, blank=True)
    need = models.TextField("Need", null=True, blank=True)
    link = models.CharField("Link", max_length=255, null=True, blank=True)
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    time = models.CharField("Time", max_length=75, null=True, blank=True)
    contact = models.CharField("Contact", max_length=255, null=True, blank=True)
    location = models.CharField("Location", max_length=255, null=True, blank=True)
    solved = models.BooleanField("Solved", default=False)
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)

    class Meta:
        ordering = ['created_on', '-solved']
        db_table = "needs"
        verbose_name = "Need"
        verbose_name_plural = "Needs"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
