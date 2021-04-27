from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('healths.urls', namespace='healths')),
    path('api/', include('healths_api.urls', namespace='healths_api')),
    path('', include('symptoms.urls', namespace='symptoms')),
    # path('api/', include('symptoms_api.urls', namespace='symptoms_api')),
    path('', include('partners.urls', namespace='partners')),
    # path('api/', include('partners_api.urls', namespace='partners_api'))
]
