from django.db import models
from django.urls import reverse


class ActivityReport(models.Model):
    """
    Activity Reports
    """

    type = models.ForeignKey('Activity', db_index=True, help_text="Type of activity you would like to report.")
    area = models.ForeignKey('Area', db_index=True, on_delete=models.CASCADE)

    address = models.CharField("Address", max_length=255)
    content = models.TextField("Report", help_text="If this is a life-threatening emergency, please notify emergency services.")
    resolved = models.BooleanField("Resolved", default=False, db_index=True)
    district = models.CharField("District", max_length=255, db_index=True)

    reporter_name = models.CharField("Reporter name", max_length=255)
    reporter_email = models.EmailField("Reporter email", null=True, blank=True)
    reporter_number = models.CharField("Reporter number", max_length=75, null=True, blank=True)

    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)
    updated_on = models.DateTimeField("Updated on", auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_on', '-resolved']
        db_table = "activity_reports"
        verbose_name = "Activity Report"
        verbose_name_plural = "Acivity Reports"

    def get_absolute_url(self):
        return reverse('tracker:activity_report_detail', kwargs={'slug': self.area.slug, 'pk': self.id})

    def __str__(self):
        return "{activity} near {area}".format(activity=self.type.name, area=self.area)

    def __unicode__(self):
        return "{activity} near {area}".format(activity=self.type.name, area=self.area)