from rest_framework import serializers
from tracker.models import ActivityReport


class ActivityReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityReport
        fields = (
            'id',
            'type',
            'area',
            'address',
            'district',
            'content',
            'resolved',
            'created_on'
        )
        read_only_field = ('id',)