from django.db import models


class HelpLine(models.Model):
    place = models.CharField("Place", max_length=255)
    title = models.CharField("Title", max_length=255)
    content = models.TextField("Content")
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)

    class Meta:
        db_table = "help_lines"
