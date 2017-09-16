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
            'dropoff_instructions',
            'resolved'
        )
        read_only_fields = (
            'id',
            'resolved',
            'created_on'
        )
