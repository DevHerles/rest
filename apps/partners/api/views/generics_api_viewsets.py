from rest_framework import viewsets
from apps.partners.models import Organ
from apps.partners.api.serializers.generics_api_serializers import (
    OrganSerializer, OrganicUnitSerializer, WorkTypeSerializer)


class OrganViewSet(viewsets.GenericViewSet):
    model = Organ
    serializer_class = OrganSerializer


class OrganicUnitViewSet(viewsets.GenericViewSet):
    serializer_class = OrganicUnitSerializer


class WorkTypeViewSet(viewsets.GenericViewSet):
    serializer_class = WorkTypeSerializer
