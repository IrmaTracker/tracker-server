from rest_framework import serializers
from forum.models import Topic


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = (
            'name',
            'content'
        ),
        read_only_fields = (
            'id',
            'slug'
            'date'
        )