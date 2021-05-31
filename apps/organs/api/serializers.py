from apps.organs.models import Organ
from rest_framework import serializers


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        exclude = ('is_active', 'created_date', 'modified_date',
                   'deleted_date', 'owner')

    def to_representation(self, instance):
        return {
            'value': instance.id,
            'label': f'{instance.code} - {instance.description}'
        }
