from rest_framework import serializers
from tracker.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = (
            'id',
            'name',
            'description'
        )
        read_only_field = ('id',)