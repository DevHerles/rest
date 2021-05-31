from rest_framework.routers import DefaultRouter
from apps.organic_units.api.viewsets import OrganicUnitViewSet
router = DefaultRouter()

router.register(r'', OrganicUnitViewSet, basename='organic_units')

urlpatterns = router.urls
