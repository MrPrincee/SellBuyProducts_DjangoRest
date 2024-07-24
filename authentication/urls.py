from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import RegisterViewSet, LoginViewSet, LogoutViewSet

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('logout', LogoutViewSet,basename='logout')

urlpatterns = [
    path('', include(router.urls)),
]