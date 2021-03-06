from django.db import models


class Post(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    link = models.CharField("Link", max_length=255, null=True, blank=True)
    time = models.CharField("Time", max_length=75, null=True, blank=True)
    place = models.CharField("Place", max_length=255, null=True, blank=True)
    status = models.CharField("Status", max_length=255, null=True, blank=True)
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-id']
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
