from django.db import models


class Supply(models.Model):
    name = models.CharField("Item name", max_length=250)

    class Meta:
        db_table = "supplies"
        verbose_name = "Supply"
        verbose_name_plural = "Supplies"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
