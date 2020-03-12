from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from bookstore.auth_.models import MyUser
from bookstore.auth_.serializers import UserSerializer


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = AllowAny,

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
