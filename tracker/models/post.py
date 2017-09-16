from django.db import models


class Post(models.Model):
    name = models.CharField("Name", max_length=255)
    link = models.URLField("Link")
    time = models.CharField("Time", max_length=75)
    status = models.CharField("Status", max_length=255)

    class Meta:
        ordering = ['-id']
        db_table = "posts"
