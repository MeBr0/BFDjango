from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from .views import UserCreateViewSet

router = SimpleRouter()

router.register('register', UserCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
]
