from django.db import models


class Base(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)
    updated_on = models.DateTimeField("Updated on", auto_now=True, editable=False)

    class Meta:
        abstract = True