from rest_framework import serializers
from tracker.models import Supply


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ('id', 'name',)