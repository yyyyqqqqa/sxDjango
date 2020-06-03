


from rest_framework import routers
from .views import RoleViewSet

router = routers.DefaultRouter()
router.register(r'', RoleViewSet, basename='role')

urlpatterns = router.urls