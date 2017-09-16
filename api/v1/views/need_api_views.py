from rest_framework import viewsets
from callapp.models import Need
from api.v1.serializers import NeedSerializer


class NeedViewSet(viewsets.ModelViewSet):
    queryset = Need.objects.all()
    serializer_class = NeedSerializer
