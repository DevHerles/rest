from apps.organic_units.models import OrganicUnit
from rest_framework import serializers


class OrganicUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganicUnit
        exclude = ('is_active', 'created_date', 'modified_date',
                   'deleted_date', 'owner')

    def to_representation(self, instance):
        return {
            'value': instance.id,
            'label': f'{instance.code} - {instance.description}'
        }
