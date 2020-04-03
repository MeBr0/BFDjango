from rest_framework import serializers

from todo.auth_.serializers import UserSerializer
from todo.main.models import ToDoList, ToDo


class ToDoListSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'owner', )


class ToDoSerializer(serializers.ModelSerializer):

    list = ToDoListSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'name', 'created_at', 'due_on', 'is_done', 'list', 'notes')
