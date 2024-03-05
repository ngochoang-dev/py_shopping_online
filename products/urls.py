from django.urls import path, include
from .views import ProductListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductListView, basename='product_view')


urlpatterns = router.urls