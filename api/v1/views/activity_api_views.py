from rest_framework import viewsets
from tracker.models import Activity
from api.v1.serializers import ActivitySerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
