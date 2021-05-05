from healths.models import Health
from .serializers import HealthSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class HealthUserWritePermission(BasePermission):
  message = 'Editing records is resctricted to the author only.'

  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True

    return obj.owner == request.user


class HealthList(viewsets.ModelViewSet):
  permission_classes =[IsAuthenticated]
  serializer_class = HealthSerializer

  # queryset = Health.postobjects.all()

  def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Health, id=item)

  # Define Custom Queryset
  def get_queryset(self):
      return Health.objects.all()


  # def list(self, request):
  #   serializer_class = HealthSerializer(self.queryset, many=True)
  #   return Response(serializer_class.data)

  # def retrieve(self, request, pk=None):
  #   health = get_object_or_404(self.queryset, pk=pk)
  #   serializer_class = HealthSerializer(health)
  #   return Response(serializer_class.data)

# class HealthList(generics.ListCreateAPIView):
#   permission_classes = [DjangoModelPermissions]
#   queryset = Health.postobjects.all()
#   serializer_class = HealthSerializer

# class HealthDetail(generics.RetrieveUpdateDestroyAPIView, HealthUserWritePermission):
#   permission_classes = [HealthUserWritePermission]
#   queryset = Health.objects.all()
#   serializer_class = HealthSerializer