from django.contrib import admin
from apps.symptoms.models import Symptom

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('id', 'q1', 'q2', 'q3', 'q4',
                    'q5', 'q6', 'q6_detail','fit','owner','partner')
