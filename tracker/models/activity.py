from django.db import models


class Activity(models.Model):
    """
    Activity
    """
    name = models.CharField("Activity name", max_length=75)
    description = models.TextField("Activity description", null=True, blank=True)

    class Meta:
        db_table = "activities"
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name