from rest_framework.routers import DefaultRouter
from apps.partners.api.views.partners_api_viewsets import PartnerViewSet
router = DefaultRouter()

router.register(r'', PartnerViewSet, basename='partners')

urlpatterns = router.urls
