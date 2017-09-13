from rest_framework import viewsets
from tracker.models import SupplySharing
from api.v1.serializers import SupplyShareSerializer


class SupplySharingViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options', 'put']
    queryset = SupplySharing.objects.all()
    serializer_class = SupplyShareSerializer

    def get_queryset(self):
        resolved_param = self.request.GET.get('resolved')
        resolved = resolved_param.lower() if resolved_param else None
        if resolved:
            return SupplySharing.objects.filter(resolved=True)
        return SupplySharing.objects.all()