from rest_framework.routers import DefaultRouter
from apps.settings.api.viewsets import SettingViewSet
router = DefaultRouter()

router.register(r'', SettingViewSet, basename='settings')

urlpatterns = router.urls
