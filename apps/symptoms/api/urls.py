from django.urls import path
from apps.symptoms.api.views import symptoms_api_view, symptom_detail_api_view

urlpatterns = [
    path('', symptoms_api_view, name='symptoms_api'),
    path('<int:pk>/', symptom_detail_api_view, name='symptom_detail_api_view'),
]
