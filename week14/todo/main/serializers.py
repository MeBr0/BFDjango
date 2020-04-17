from rest_framework import serializers

from todo.auth_.serializers import UserSerializer
from todo.main.models import ToDoList, ToDo


class NameableSerializer(serializers.ModelSerializer):

    """
    Stupid example of serializer inheritance
    """
    class Meta:
        model = ToDoList
        fields = ('id', 'name',)


class ToDoListSerializer(NameableSerializer):

    owner = UserSerializer(read_only=True)

    class Meta(NameableSerializer.Meta):
        fields = NameableSerializer.Meta.fields + ('owner', )


class ToDoSerializer(NameableSerializer):

    list = ToDoListSerializer(read_only=True)

    class Meta(NameableSerializer.Meta):
        model = ToDo
        fields = NameableSerializer.Meta.fields + ('created_at', 'due_on', 'is_done', 'list', 'notes', 'attachment',)
