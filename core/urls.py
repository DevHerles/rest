from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout, UserToken

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de API",
        default_version='v0.1',
        description="Documentación pública de API de Ecommerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="developerpeperu@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/settings/', include('apps.settings.api.urls')),
    path('api/users/', include('apps.users.api.urls')),
    path('api/healths/', include('apps.healths.api.urls')),
    path('api/symptoms/', include('apps.symptoms.api.urls')),
]
