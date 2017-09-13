from rest_framework import viewsets
from forum.models import Topic
from api.v1.serializers import TopicSerializer


class AnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
