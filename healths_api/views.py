from rest_framework import generics
from healths.models import Health
from .serializers import HealthSerializer
from rest_framework.permissions import IsAdminUser

class HealthList(generics.ListCreateAPIView):
  permission_classes = [IsAdminUser]
  queryset = Health.postobjects.all()
  serializer_class = HealthSerializer

class HealthDetail(generics.RetrieveDestroyAPIView):
  queryset = Health.objects.all()
  serializer_class = HealthSerializer