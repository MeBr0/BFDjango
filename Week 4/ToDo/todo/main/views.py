from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from todo.main.models import ToDo, ToDoList
from todo.main.serializers import ToDoSerializer, ToDoListSerializer


class ToDoListsView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ToDoListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class ToDoListView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return ToDoList.objects.for_user(self.request.user).filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return ToDoListSerializer


class ToDosView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return ToDo.objects.filter(list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return ToDoSerializer

    def perform_create(self, serializer):
        list_id = self.kwargs.get('pk')
        serializer.save(list=ToDoList.objects.get(id=list_id))


class ToDoView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return ToDo.objects.filter(id=self.kwargs.get('pk'), list=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return ToDoSerializer
