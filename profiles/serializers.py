from rest_framework import serializers
from profiles.models import Profiles


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'
