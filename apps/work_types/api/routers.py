from rest_framework.routers import DefaultRouter
from apps.work_types.api.viewsets import WorkTypeViewSet
router = DefaultRouter()

router.register(r'', WorkTypeViewSet, basename='work_types')

urlpatterns = router.urls
