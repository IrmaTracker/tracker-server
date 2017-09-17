from rest_framework import serializers
from callapp.models import Need


class NeedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Need
        fields = ('name', 'need', 'need_id', 'time', 'contact', 'location', 'lat', 'long')