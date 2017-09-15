from rest_framework import serializers
from tracker.models import SupplySharing


class SupplyShareSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplySharing
        fields = (
            'id',
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'shareable_supplies',
            'pickup_instructions',
            'lat',
            'long',
            'time',
            'contact',
            'request',
            'resolved'
        )
        read_only_fields = (
            'id',
            'resolved',
            'created_on'
        )
