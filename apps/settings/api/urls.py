from django.urls import path
from apps.settings.api.views import settings_api_view, setting_detail_api_view

urlpatterns = [
    path('', settings_api_view, name='settings_api'),
    path('<int:pk>/', setting_detail_api_view, name='setting_detail_api_view'),
]
