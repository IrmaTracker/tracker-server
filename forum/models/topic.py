from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from .base import Base


class Topic(Base):
    name = models.CharField("Name", max_length=255, unique=True)
    slug = models.SlugField("Slug", db_index=True, unique=True, editable=False)
    date = models.DateField("Date", auto_now_add=True, editable=False)
    content = RichTextField("Content")

    def get_absolute_url(self):
        return reverse('news:topic_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

    class Meta:
        db_table = 'topics'
        ordering = ['-created_on', '-updated_on']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
