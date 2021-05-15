from django.urls import path
from apps.healths.api.views import healths_api_view, health_detail_api_view

urlpatterns = [
    path('', healths_api_view, name='healths_api'),
    path('<int:pk>/', health_detail_api_view, name='health_detail_api_view'),
]
