from .views import ProfileList
from rest_framework.routers import DefaultRouter

app_name = 'profile_api'

router = DefaultRouter()
router.register('', ProfileList, basename='profile')
urlpatterns = router.urls

# urlpatterns = [
#     path('', HealthList.as_view(), name='listcreate'),
#     path('<int:pk>/', HealthDetail.as_view(), name='detailcreate'),
# ]
