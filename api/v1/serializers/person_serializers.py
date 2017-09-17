from rest_framework import serializers
from tracker.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'age',
            'phonenumber',
            'missing_since',
            'marked_safe_on',
            'marked_safe_by',
            'district',
            'address',
            'area',
            'safe',
            'extra_info',
            'requester_name',
            'requester_email',
            'requester_fb',
            'requester_number',
            'emergency_contact_name',
            'emergency_contact_number',
            'duplicate',
            'created_on'
        )