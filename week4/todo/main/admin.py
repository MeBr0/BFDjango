from django.contrib import admin

from todo.main.models import ToDoList, ToDo


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', )


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('name', 'list', 'created_at', 'notes', 'is_done', )
