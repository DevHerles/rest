from rest_framework import serializers

from django.conf import settings
from apps.partners.models import Partner


class PartnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )

    def create(self, validated_data):
        print('validated_data', validated_data)
        partner = Partner(**validated_data)
        partner.save()
        return partner


class PartnerAffidavitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'partner_type': instance.partner_type,
            'doc_number': instance.doc_number,
            'doc_type': instance.doc_type,
            'name': instance.name,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
        }


class PartnerSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format='%Y-%m-%d',
                                input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Partner
        exclude = (
            'is_active',
            'created_date',
            'modified_date',
            'deleted_date',
        )

    def to_representation(self, instance):
        return {
            'id':
            instance.id,
            'partner_type':
            instance.partner_type if instance.partner_type else '',
            'doc_number':
            instance.doc_number if instance.doc_number else '',
            'doc_type':
            instance.doc_type if instance.doc_type else '',
            'name':
            instance.name if instance.name else '',
            'first_name':
            instance.first_name if instance.first_name else '',
            'last_name':
            instance.last_name if instance.last_name else '',
            'dob':
            instance.dob if instance.dob else '',
            'email':
            instance.email if instance.email else '',
            'phone':
            instance.phone if instance.phone else '',
            'organ':
            instance.organ.id if instance.organ else '',
            'organic_unit':
            instance.organic_unit.id if instance.organic_unit else '',
            'functional_team':
            instance.functional_team if instance.functional_team else '',
            'position':
            instance.position if instance.position else '',
            'work_type':
            instance.work_type.id if instance.work_type else '',
            'owner':
            instance.owner.id if instance.owner else ''
        }
