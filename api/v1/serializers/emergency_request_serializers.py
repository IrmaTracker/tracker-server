from rest_framework import serializers
from tracker.models import EmergencyRequest


class EmergencyRequestSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = EmergencyRequest
        fields = (
            'id',
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'has_24_hours',
            'has_injuries',
            'has_rain_shelter',
            'has_lod_situation',
            'additional_persons',
            'days_of_food',
            'days_of_water',
            'requires_medical_supplies',
            'medical_supplies',
            'type_of_injuries',
            'request',
            'lat',
            'long',
            'time',
            'contact'
        )
        read_only_fields = (
            'resolved',
            'created_on'
        )
