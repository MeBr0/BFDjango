from django.urls import path

from .views import ToDoListsView, ToDoListView, ToDosView, ToDoView

urlpatterns = [
    path('', ToDoListsView.as_view()),
    path('<int:pk>/', ToDoListView.as_view()),
    path('<int:pk>/todo/', ToDosView.as_view()),
    path('<int:pk2>/todo/<int:pk>/', ToDoView.as_view()),
]
