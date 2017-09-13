from rest_framework import viewsets
from tracker.models import EmergencyRequest
from api.v1.serializers import EmergencyRequestSerializer


class EmergencyRequestViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options', 'put']
    queryset = EmergencyRequest.objects.all()
    serializer_class = EmergencyRequestSerializer

    def get_queryset(self):
        resolved_param = self.request.GET.get('resolved')
        resolved = resolved_param.lower() if resolved_param else None
        if resolved:
            return EmergencyRequest.objects.filter(resolved=True)
        return EmergencyRequest.objects.all()