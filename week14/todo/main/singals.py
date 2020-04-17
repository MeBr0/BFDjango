from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.main.models import ToDoList, ToDo


@receiver(post_save, sender=ToDoList)
def create_task_in_task_list(sender, instance, created, **kwargs):
    """
    If list created, add empty item in it
    """
    if created:
        ToDo.objects.create(name='Empty todo', list=instance)
