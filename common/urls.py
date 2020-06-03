
from rest_framework import routers
from .views import CommonViewSet

router = routers.DefaultRouter()
router.register(r'', CommonViewSet, basename='common')

urlpatterns = router.urls