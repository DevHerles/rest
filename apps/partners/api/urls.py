from django.urls import path
from apps.partners.api.views.generics_api_views import (OrganListAPIView,
                                                        OrganicUnitListAPIView,
                                                        WorkTypeListAPIView)
from apps.partners.api.views.partners_api_views import (
    PartnerListCreateAPIView,
    PartnerRetrieveUpdateDestroyAPIView,
)
urlpatterns = [
    path('', PartnerListCreateAPIView.as_view(), name='partners'),
    path('<int:pk>/',
         PartnerRetrieveUpdateDestroyAPIView.as_view(),
         name='partner_retrieve_update_destroy'),
    path('organs/', OrganListAPIView.as_view(), name='organs'),
    path('organic_units/',
         OrganicUnitListAPIView.as_view(),
         name='organic_units'),
    path('work_types/', WorkTypeListAPIView.as_view(), name='work_types'),
]
