from rest_framework import serializers
from callapp.models import Need


class NeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Need
        fields = ('need', 'need_id', 'link', 'name', 'time', 'contact', 'location', 'lat', 'long')