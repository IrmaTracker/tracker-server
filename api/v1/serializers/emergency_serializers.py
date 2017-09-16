from rest_framework import serializers
from tracker.models import Emergency


class EmergencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Emergency
        fields = ('status', 'name', 'time', 'solved', 'lat', 'long')