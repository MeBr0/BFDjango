from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny

from todo.auth_.models import MyUser
from todo.auth_.serializers import UserSerializer


class UserCreateViewSet(GenericViewSet, CreateModelMixin):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserSerializer
