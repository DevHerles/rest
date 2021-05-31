from rest_framework.routers import DefaultRouter
from apps.organs.api.viewsets import OrganViewSet
router = DefaultRouter()

router.register(r'', OrganViewSet, basename='organs')

urlpatterns = router.urls
