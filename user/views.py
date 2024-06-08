from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.

# User Views from api all crud operations

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentInfoViewSet(viewsets.ModelViewSet):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer