from rest_framework import serializers
from callapp.models import Emergency


class EmergencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Emergency
        fields = ('status', 'name', 'link', 'place', 'time', 'solved')