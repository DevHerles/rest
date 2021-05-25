from django.contrib import admin
from apps.healths.models import Health

class HealthAdmin(admin.ModelAdmin):
    list_display = ('id', 'q1', 'q2', 'q3', 'q4',
                    'q5', 'q6', 'q7', 'q8',
                    'q9', 'q10', 'q11', 'q12', 'q12_detail','fit','owner','partner')


admin.site.register(Health, HealthAdmin)
