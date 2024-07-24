from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CreateProductViewSet, SellProductViewSet, BuyProductViewSet

router = DefaultRouter()
router.register("products",CreateProductViewSet,basename='products')
router.register("sell_products",SellProductViewSet,basename='sell_products')
router.register("buy_products",BuyProductViewSet,basename="buy_products")

urlpatterns = [
    path('', include(router.urls)),
]