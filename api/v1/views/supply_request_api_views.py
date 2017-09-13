from rest_framework import viewsets
from tracker.models import SupplyRequest
from api.v1.serializers import SupplyRequestSerializer


class SupplyRequestViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options', 'put']
    queryset = SupplyRequest.objects.all()
    serializer_class = SupplyRequestSerializer

    def get_queryset(self):
        resolved_param = self.request.GET.get('resolved')
        resolved = resolved_param.lower() if resolved_param else None
        if resolved:
            return SupplyRequest.objects.filter(resolved=True)
        return SupplyRequest.objects.all()

