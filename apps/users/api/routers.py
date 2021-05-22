from rest_framework.routers import DefaultRouter
from apps.users.api.viewsets import UserViewSet

router = DefaultRouter()

router.register(r'', UserViewSet, basename='userss')

urlpatterns = router.urls
