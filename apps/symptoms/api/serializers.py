from rest_framework import serializers
from apps.symptoms.models import Symptom
from apps.healths.models import TypeOfResponse


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

    def create(self, validated_data):
        symptom = Symptom(**validated_data)
        for key in validated_data:
            if validated_data[key] == TypeOfResponse.YES:
                symptom.fit = False
                break
        symptom.save()
        return symptom


class SymptomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         'id': instance['id'],
    #         'username': instance['username'],
    #         'email': instance['email'],
    #         'password': instance['password']
    #     }