from django.db import models


class Emergency(models.Model):
    """
    CallApp Table
    """

    status = models.CharField("Status", max_length=255, null=True, blank=True)
    link = models.CharField("Link", max_length=255, null=True, blank=True)
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    time = models.CharField("Time", max_length=75, null=True, blank=True)
    place = models.CharField("Place", max_length=255, null=True, blank=True)
    solved = models.BooleanField("Solved", default=False)
    created_on = models.DateTimeField("Created on", auto_now_add=True)

    class Meta:
        ordering = ['-id']
        db_table = "emergencies"
        verbose_name = "Emergency"
        verbose_name_plural = "Emergencies"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name