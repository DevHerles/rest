from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.organic_units.api.serializers import (
    OrganicUnitSerializer, )


class OrganicUnitViewSet(viewsets.GenericViewSet):
    serializer_class = OrganicUnitSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
