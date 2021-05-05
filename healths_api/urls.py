from .views import HealthList
from rest_framework.routers import DefaultRouter

app_name = 'health_api'

router = DefaultRouter()
router.register('', HealthList, basename='healths')
urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', HealthDetail.as_view(), name='detailcreate'),
#     path('', HealthList.as_view(), name='listcreate'),
# ]
