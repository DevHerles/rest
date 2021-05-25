from rest_framework.routers import DefaultRouter
from apps.symptoms.api.viewsets import SymptomViewSet
router = DefaultRouter()

router.register(r'', SymptomViewSet, basename='symptoms')

urlpatterns = router.urls
