

from rest_framework import routers
from .views import MenuViewSet

router = routers.DefaultRouter()
router.register(r'', MenuViewSet, basename='menu')

urlpatterns = router.urls