from rest_framework import serializers
from tracker.models import SupplyRequest


class SupplyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplyRequest
        fields = (
            'id',
            'full_name',
            'address',
            'district',
            'contact_numbers',
            'supplies',
            'quantity',
            'dropoff_instructions'
        )
        read_only_fields = (
            'resolved',
            'created_on'
        )
