from django.db import models


class Post(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    link = models.URLField("Link", null=True, blank=True)
    time = models.CharField("Time", max_length=75, null=True, blank=True)
    status = models.CharField("Status", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-id']
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
