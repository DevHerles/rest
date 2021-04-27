from rest_framework import generics
from healths.models import Health
from .serializers import HealthSerializer

class HealthList(generics.ListCreateAPIView):
  queryset = Health.postobjects.all()
  serializer_class = HealthSerializer

class HealthDetail(generics.RetrieveDestroyAPIView):
  queryset = Health.objects.all()
  serializer_class = HealthSerializer