from rest_framework import generics
from healths.models import Health
from .serializers import HealthSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions

class HealthList(generics.ListCreateAPIView):
  permission_classes = [DjangoModelPermissions]
  queryset = Health.postobjects.all()
  serializer_class = HealthSerializer

class HealthDetail(generics.RetrieveDestroyAPIView):
  queryset = Health.objects.all()
  serializer_class = HealthSerializer