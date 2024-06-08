from django.urls import path
from .views import PrimaryRequest, SecondaryRequest


urlpatterns = [
    path('PrimaryRequest/', PrimaryRequest.as_view()),  
    path('SecondaryRequest/<int:pk>/', SecondaryRequest.as_view()),  
]
