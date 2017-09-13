from django.db import models
from tracker.constants import *
from tracker.models import AbstractRequestBase


class Answer:
    NO = 0
    YES = 1


class EmergencyRequest(AbstractRequestBase):
    YESNO = (
        (0, "No"),
        (1, "Yes")
    )

    SUPPLY_DAYS = (
        (0, "None"),
        (1, "Enough for 1 day"),
        (2, "Enough for 2 days"),
        (3, "Enough for more than 3 days"),
    )

    has_24_hours = models.IntegerField("Will you survive the next 24 hours?", choices=YESNO, default=1, db_index=True)
    has_injuries = models.IntegerField("Do you have a physical injury?", choices=YESNO, default=0, db_index=True)
    has_rain_shelter = models.IntegerField("Does your location have shelter from the rain?", choices=YESNO, default=0, db_index=True)
    has_lod_situation = models.IntegerField("Are any of you in a life or death situation?", choices=YESNO, default=0, db_index=True)

    additional_persons = models.TextField("Additional Persons", null=True, blank=True, help_text=ADDITIONAL_PERSONS)
    days_of_food = models.IntegerField("Days of food", choices=SUPPLY_DAYS, help_text=DO_FOOD, default=3)
    days_of_water = models.IntegerField("Days of drinking water", choices=SUPPLY_DAYS, help_text=DO_WATER, default=3)

    requires_medical_supplies = models.IntegerField("Does anyone need immediate medical supplies?", choices=YESNO, default=0)
    medical_supplies = models.TextField("Immediate medical supplies", null=True, blank=True, help_text=MEDICAL_SUPPLIES_TF)

    type_of_injuries = models.TextField("Type of injuries", null=True, blank=True, help_text=TYPE_OF_INJURIES)

    request = models.TextField("In short, can you describe your emergency and/or request")

    urgency_ranking = models.IntegerField("Urgency ranking", default=5, db_index=True)

    def save(self, *args, **kwargs):
        self.urgency_ranking = self.get_request_ranking()
        super(EmergencyRequest, self).save(*args, **kwargs)

    def get_request_ranking(self):
        # Ideally we would be using BooleanField instead of IntegerField
        # but, it looks like some folk need EXPLICIT `Yes/No` selectors, so...
        # Yay, work around!

        # The is here just to prioritize some of the most critical
        # requests. For now, any other ranking will be done manually on the dashboard.
        # TODO: Clean this up - it's gross.

        # life or death situations are automatically priority 1
        if self.has_lod_situation == Answer.YES or \
                (self.has_injuries == Answer.YES and self.has_24_hours == Answer.NO):
            return 1

        # has injuries but will survive the next 24 hours
        if self.has_injuries == Answer.YES and self.has_24_hours == Answer.YES or \
                (self.requires_medical_supplies == Answer.YES):
            return 2
        return 5

    class Meta:
        db_table = "emergency_requests"
        ordering = ['urgency_ranking', 'resolved']
        verbose_name = "Emergency Request"
        verbose_name_plural = "Emergency Requests"
        unique_together = (
            ('address', 'district', 'contact_numbers'),
        )
        index_together = (
            ('urgency_ranking', 'resolved'),
        )

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name
