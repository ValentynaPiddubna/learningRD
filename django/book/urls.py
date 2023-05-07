from rest_framework.routers import SimpleRouter
from .views import BookViewSet
from django.urls import path


urlpatterns = []

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls

