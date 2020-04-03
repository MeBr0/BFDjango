from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from .views import UserCreateViewSet

router = DefaultRouter()

router.register(r'register', UserCreateViewSet, basename='register')

urlpatterns = [
    path('login/', obtain_jwt_token),
]

urlpatterns += router.urls
