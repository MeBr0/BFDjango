from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from bookstore.auth_.models import MyUser
from bookstore.auth_.serializers import UserSerializer


# ViewSet for user creation
class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = AllowAny,
