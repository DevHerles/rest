from .views import HealthList
from rest_framework.routers import DefaultRouter

app_name = 'health_api'

router = DefaultRouter()
router.register('', HealthList, basename='health')
urlpatterns = router.urls

# urlpatterns = [
#     path('', HealthList.as_view(), name='listcreate'),
#     path('<int:pk>/', HealthDetail.as_view(), name='detailcreate'),
# ]
