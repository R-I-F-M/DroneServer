from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentInfoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paymentinfo', PaymentInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]