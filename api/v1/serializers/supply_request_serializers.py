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
            'district_admin',
            'contact_numbers',
            'supplies',
            'quantity',
            'dropoff_instructions',
            'resolved'
        )
        read_only_fields = (
            'id',
            'district_admin',
            'resolved',
            'created_on'
        )
