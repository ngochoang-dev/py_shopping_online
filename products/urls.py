from django.urls import path, include
from .views import ProductListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductListView, basename='xx')


urlpatterns = router.urls