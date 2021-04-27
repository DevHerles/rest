from django.contrib import admin
from django.urls import path
from .views import HealthList, HealthDetail

app_name = 'health_api'

urlpatterns = [
    path('<int:pk>/', HealthDetail.as_view(), name='detailcreate'),
    path('', HealthList.as_view(), name='listcreate'),
]
