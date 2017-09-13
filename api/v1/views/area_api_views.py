from rest_framework import viewsets
from tracker.models import Area
from api.v1.serializers import AreaSerializer


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
