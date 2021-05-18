from rest_framework import serializers

from apps.partners.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = (
            'active',
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
            'dob': instance.dob,
            'email': instance.email,
            'phone': instance.phone,
            'organ_id': instance.organ_id.code or '',
            'organic_unit_id': instance.organic_unit_id.code or '',
            'functional_team': instance.functional_team,
            'position': instance.position,
            'work_type_id': instance.work_type_id.code or '',
            'user_id': instance.user_id.id
        }
