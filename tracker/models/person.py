from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import smart_text
from django.conf import settings
from tracker.mailer import MG

# MailGun Client
mg = MG()


class Person(models.Model):
    age = models.IntegerField("Age", null=True, blank=True)
    name = models.CharField("Name", max_length=255, db_index=True)
    photo = models.ImageField('Image', null=True, blank=True, upload_to='images/')
    district = models.CharField("District", max_length=255, null=True, blank=True)
    address = models.CharField("Address", max_length=255, help_text="The person's address", null=True, blank=True)
    phonenumber = models.CharField("Phone number", max_length=75, help_text="The person's phone number", null=True, blank=True)
    safe = models.BooleanField("Safe", default=False, db_index=True)
    marked_safe_by = models.CharField("Marked safe by", max_length=126, null=True, blank=True, help_text="Name of the person checking this box")
    marked_safe_on = models.DateTimeField("Marked safe on", null=True, blank=True, editable=False)
    area = models.ForeignKey('Area', db_index=True)
    missing_since = models.CharField('Missing since', max_length=255, null=True, blank=True)
    requester_name = models.CharField('Your Name', max_length=255, null=True, blank=True)
    requester_fb = models.URLField('Your Facebook Profile', null=True, blank=True)
    requester_number = models.CharField('Your Number', max_length=75, null=True, blank=True)
    requester_email = models.EmailField('Your Email', null=True, blank=True)
    emergency_contact_name = models.CharField("Emergency Contact Name", max_length=255, null=True, blank=True)
    emergency_contact_number = models.CharField("Emergency Contact Number", max_length=255, null=True, blank=True)
    extra_info = models.TextField("Extra info", null=True, blank=True)
    created_on = models.DateTimeField("Created on", auto_now_add=True, editable=False)
    notified = models.BooleanField("Notified", default=False, editable=False)

    def get_absolute_url(self):
        return reverse('tracker:update_person', kwargs={'slug': self.area.slug, 'pk': self.id})

    @property
    def safe_display(self):
        return "Marked safe" if self.safe else "Unknown"

    def save(self, *args, **kwargs):
        if self.safe:
            self.marked_safe_on = timezone.now()
        else:
            self.marked_safe_on = None

        if self.safe and self.requester_email and not self.notified:
            # This is bad, but seeing
            # that we're not going to get Celery running anytime
            # soon, we'll just make the synchronous API call to mailgun and keep on moving.
            # We'll scale up if we have to to handle the load while the web workers are waiting
            # for the request to complete.
            self.notify_requester()
            self.notified = True
        else:
            # this is really dumb, but some users are marking people
            # as safe accidentally, when that happens, we need to reset...
            self.notified = False
        super(Person, self).save(*args, **kwargs)

    class Meta:
        db_table = "persons"
        ordering = ['name']

    def notify_requester(self):
        """
        Yes, I too, noticed that the message was short and sweet.
        """
        name = smart_text(self.name)
        email = self.requester_email
        marked_safe_by = self.marked_safe_by
        domain_name = settings.DOMAIN_NAME
        irma_link = "{domain}{path}".format(domain=domain_name, path=self.get_absolute_url())

        subject = "Irma Tracker: Marked Safe Notification"

        email_body = "{irma_link}\n" \
                     "{name} was marked safe by {marked_safe_by}. \n\n" \
                     "Please spread the word about {domain} so that others " \
                     "may locate their loved ones as well.".format(name=name, marked_safe_by=marked_safe_by,
                                                                   irma_link=irma_link, domain=domain_name)
        return mg.send(subject, email, email_body)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
