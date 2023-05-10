from rest_framework.routers import SimpleRouter
from .views import UserViewSet

urlpatterns = []

router = SimpleRouter()
router.register('', UserViewSet, basename='users')

urlpatterns += router.urls


