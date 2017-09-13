from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from tracker.models import Person
from api.v1.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options', 'put']
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @list_route(methods=['GET'])
    def safe(self, request):
        """
        Returns a list of people who were marked safe
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def missing(self, request):
        """
        Returns a list of missing persons
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'])
    def search(self, request):
        """
        Search for a person by name
        """
        name = request.GET.get('name')
        if not name:
            empty = {
                "count": 0,
                "next": None,
                "previous": None,
                "results": []
            }
            return Response(empty)

        person_queryset = Person.objects.filter(name__icontains=name)
        queryset = self.filter_queryset(person_queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        area_id = self.get_area_id()
        if self.action == 'safe':
            queryset = Person.objects.filter(safe=True)
        elif self.action == 'missing':
            queryset = Person.objects.filter(safe=False)
        else:
            queryset = Person.objects.all()

        # if we get a request like `/api/v1/persons?area=1`
        # we'll filter persons by area.
        if area_id:
            return queryset.filter(area_id=area_id)
        return queryset

    def get_area_id(self):
        try:
            area = self.request.GET.get('area') if self.request.GET.get('area') else None
            if area:
                return int(area)
            return None
        except ValueError:
            return None

