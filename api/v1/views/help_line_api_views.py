from rest_framework import viewsets
from callapp.models import HelpLine
from api.v1.serializers import HelpLineSerializer


class HelpLineViewSet(viewsets.ModelViewSet):
    queryset = HelpLine.objects.all()
    serializer_class = HelpLineSerializer
