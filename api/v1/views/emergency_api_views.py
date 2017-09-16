from rest_framework import viewsets
from callapp.models import Emergency
from api.v1.serializers import EmergencySerializer


class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer
