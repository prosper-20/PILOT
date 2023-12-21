from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView

class ListProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



