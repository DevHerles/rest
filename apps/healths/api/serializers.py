from rest_framework import serializers
from apps.healths.models import Health
from apps.healths.models import TypeOfResponse


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

    def create(self, validated_data):
        health = Health(**validated_data)
        for key in validated_data:
            if validated_data[key] == TypeOfResponse.YES:
                health.fit = False
                break
        health.save()
        return health


class HealthListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         'id': instance['id'],
    #         'username': instance['username'],
    #         'email': instance['email'],
    #         'password': instance['password']
    #     }
