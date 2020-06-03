
from rest_framework import routers
from .views import DeptViewSet

router = routers.DefaultRouter()
router.register(r'', DeptViewSet, basename='dept')

urlpatterns = router.urls