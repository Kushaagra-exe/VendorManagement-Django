from django.urls import path
from .views import VendorViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/', VendorViewSet.as_view({'get': 'list'}), name='vendor-list'),
    path('vendors/<int:pk>/', VendorViewSet.as_view({'get': 'retrieve'}), name='vendor-detail'),
]