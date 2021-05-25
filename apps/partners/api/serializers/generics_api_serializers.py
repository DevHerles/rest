from apps.partners.models import Organ, OrganicUnit, WorkType
from rest_framework import serializers


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )


class OrganicUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganicUnit
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )
