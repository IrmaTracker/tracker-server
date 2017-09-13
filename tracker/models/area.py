from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Area(models.Model):
    name = models.CharField("Name", max_length=128, unique=True, db_index=True)
    slug = models.SlugField("Slug", unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('tracker:area_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)

    class Meta:
        db_table = "areas"
        ordering = ['name']

    def __str__(self):
        return self.name

