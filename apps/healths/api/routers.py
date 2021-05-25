from rest_framework.routers import DefaultRouter
from apps.healths.api.viewsets import HealthViewSet
router = DefaultRouter()

router.register(r'', HealthViewSet, basename='healths')

urlpatterns = router.urls
