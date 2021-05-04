from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('healths.urls', namespace='healths')),
    path('api/', include('healths_api.urls', namespace='healths_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
