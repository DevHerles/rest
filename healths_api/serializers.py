from rest_framework import serializers
from healths.models import Health

class HealthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Health
    fields = ('id', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q12_detail', 'fit', 'created_at', 'owner')