

from rest_framework import routers
from .views import StuViewSet

router = routers.DefaultRouter()
router.register(r'', StuViewSet, basename='stu')

urlpatterns = router.urls