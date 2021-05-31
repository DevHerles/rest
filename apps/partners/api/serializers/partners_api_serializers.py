from rest_framework import serializers

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
            'doc_type': instance.doc_type if instance.doc_type else '',
            'name': instance.name,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'dob': instance.dob,
            'email': instance.email,
            'phone': instance.phone,
            'organ': instance.organ.id if instance.organ else '',
            'organic_unit':
            instance.organic_unit.id if instance.organic_unit else '',
            'functional_team': instance.functional_team,
            'position': instance.position,
            'work_type': instance.work_type.id if instance.work_type else '',
            'owner': instance.owner.id if instance.owner else ''
        }
