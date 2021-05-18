from rest_framework.routers import DefaultRouter
from apps.partners.api.views.partners_api_viewsets import PartnerViewSet
from apps.partners.api.views.generics_api_viewsets import (OrganViewSet,
                                                           OrganicUnitViewSet,
                                                           WorkTypeViewSet)
router = DefaultRouter()

router.register(r'', PartnerViewSet, basename='products')
router.register(r'', OrganViewSet, basename='organs')
router.register(r'', OrganicUnitViewSet, basename='organic_units')
router.register(r'', WorkTypeViewSet, basename='work_types')

urlpatterns = router.urls
