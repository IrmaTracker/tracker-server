from rest_framework import viewsets
from tracker.models import ActivityReport
from api.v1.serializers import ActivityReportSerializer


class ActivityReportViewSet(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = ActivityReport.objects.all()
    serializer_class = ActivityReportSerializer
