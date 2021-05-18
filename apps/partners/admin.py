from django.contrib import admin
from apps.partners.models import Partner, WorkType, Organ, OrganicUnit


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'description',
    )


class OrganAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'description',
    )


class OrganicUnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'description',
    )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_name', 'last_name', 'doc_type',
                    'doc_number', 'email')


admin.site.register(Partner, PartnerAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(Organ, OrganAdmin)
admin.site.register(OrganicUnit, OrganicUnitAdmin)
