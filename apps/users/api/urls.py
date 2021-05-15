from django.urls import path
from apps.users.api.views import user_api_view, user_detail_api_view

urlpatterns = [
    path('', user_api_view, name='user_api'),
    path('<int:pk>/', user_detail_api_view, name='user_detail_api_view'),
]
