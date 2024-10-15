from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Sizeviewset, ProductViewset,AdminLoginView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'sizes', Sizeviewset, basename='size')
router.register(r'products', ProductViewset, basename='product')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('admin-login/', AdminLoginView.as_view(), name='admin_login'),
]
