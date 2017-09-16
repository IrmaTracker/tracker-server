from rest_framework import serializers
from tracker.models import HelpLine


class HelpLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpLine
        fields = ('place', 'title', 'content')