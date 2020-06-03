

from rest_framework import routers
from .views import DictTypeViewSet,DictDataViewSet

router = routers.DefaultRouter()
router.register(r'', DictTypeViewSet, basename='dictType')
router.register(r'', DictDataViewSet, basename='dictData')
urlpatterns = router.urls

