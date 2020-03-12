from rest_framework import serializers

from BookStore.auth_.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'is_super_admin', 'password', )

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = MyUser.objects.create_user(**validated_data)

        user.set_password(password)

        user.save()

        return user
