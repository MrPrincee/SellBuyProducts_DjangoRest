from django.shortcuts import render

from product.models import Products
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from product.serializers import ProductSerializer, SellProductsSerializer, BuyProductsSerializer


class CreateProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Products.objects.none()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Products.objects.filter(owner=request.user)
        user_products = list(queryset.values())
        return Response(user_products)


class SellProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SellProductsSerializer
    queryset = Products.objects.none()

    def create(self,request,*args,**kwargs):
        return super().create(request,*args,*kwargs)

    def list(self, request, *args, **kwargs):
        queryset = Products.objects.filter(owner=request.user)
        user_products = list(queryset.values())
        return Response(user_products)


class BuyProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BuyProductsSerializer
    queryset = Products.objects.none()

    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)

    def list(self,request,*args,**kwargs):
        queryset = Products.objects.filter(available_for_sale=True).exclude(owner = request.user)
        items_on_sale = list(queryset.values())
        return Response(items_on_sale)
