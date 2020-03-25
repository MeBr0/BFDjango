from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from todo.main.models import ToDo, ToDoList
from todo.main.serializers import ToDoSerializer, ToDoListSerializer


class ListViewSet(NestedViewSetMixin, ModelViewSet):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ToDoListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class TaskViewSet(NestedViewSetMixin, ModelViewSet):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.filter(list=self.kwargs.get('parent_lookup_list'))

    def get_serializer_class(self):
        return ToDoSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(list=ToDoList.objects.get(id=list_id))
