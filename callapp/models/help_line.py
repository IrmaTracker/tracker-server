from django.db import models


class HelpLine(models.Model):
    place = models.CharField("Place", max_length=255, null=True, blank=True)
    title = models.CharField("Title", max_length=255, null=True, blank=True)
    content = models.TextField("Content", null=True, blank=True)
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)

    class Meta:
        db_table = "help_lines"
