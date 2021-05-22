from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout, UserToken

schema_view = get_schema_view(
    openapi.Info(
        title="DJ-Salud API",
        default_version='v0.1',
        description="Documentación pública de API de DJ-Salud",
        terms_of_service="https://minsa.gob.pe/",
        contact=openapi.Contact(email="hincalla@minsa.gob.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/settings/', include('apps.settings.api.urls')),
    path('api/users/', include('apps.users.api.urls')),
    path('api/partners/', include('apps.partners.api.routers')),
    path('api/healths/', include('apps.healths.api.urls')),
    path('api/symptoms/', include('apps.symptoms.api.urls')),
]
