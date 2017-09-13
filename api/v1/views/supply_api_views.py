from rest_framework import viewsets
from tracker.models import Supply
from api.v1.serializers import SupplySerializer


class SupplyViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer