from apps.partners.models import WorkType
from rest_framework import serializers


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        exclude = ('is_active', 'created_date', 'modified_date',
                   'deleted_date', 'owner')

    def to_representation(self, instance):
        return {
            'value': instance.id,
            'label': f'{instance.code} - {instance.description}'
        }
