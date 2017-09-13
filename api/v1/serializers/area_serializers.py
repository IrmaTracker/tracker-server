from rest_framework import serializers
from tracker.models import Area


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'name')
        read_only_field = ('id',)