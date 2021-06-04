from rest_framework import serializers
from apps.healths.models import Health
from apps.healths.models import TypeOfResponse
from apps.partners.api.serializers.partners_api_serializers import PartnerAffidavitSerializer


class HealthCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )

    def create(self, validated_data):
        owner = validated_data.get('owner', None)
        if owner:
            validated_data['partner'] = owner.partner
        health = Health(**validated_data)
        for key in validated_data:
            if validated_data[key] == TypeOfResponse.YES:
                health.fit = False
                break
        health.save()
        return health

    def update(self, instance, validated_data):
        health = super().update(instance, validated_data)
        health.fit = True
        for key in validated_data:
            if validated_data[key] == TypeOfResponse.YES:
                health.fit = False
                break
        health.save()
        return health


class HealthSerializer(serializers.ModelSerializer):
    partner = PartnerAffidavitSerializer()

    class Meta:
        model = Health
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )

    def create(self, validated_data):
        owner = validated_data.get('owner', None)
        print('owner', owner.partner)
        if owner:
            validated_data['partner'] = owner.partner
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
