from rest_framework import generics
from healths.models import Health
from .serializers import HealthSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions


class HealthUserWritePermission(BasePermission):
  message = 'Editing records is resctricted to the author only.'

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True

    return obj.owner == request.user

class HealthList(generics.ListCreateAPIView):
  permission_classes = [DjangoModelPermissions]
  queryset = Health.postobjects.all()
  serializer_class = HealthSerializer

class HealthDetail(generics.RetrieveUpdateDestroyAPIView, HealthUserWritePermission):
  permission_classes = [HealthUserWritePermission]
  queryset = Health.objects.all()
  serializer_class = HealthSerializer