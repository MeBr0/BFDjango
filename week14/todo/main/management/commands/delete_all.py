from django.core.management import BaseCommand

from todo.main.models import ToDoList, ToDo


class Command(BaseCommand):
    """
    Delete all objects in database
    """

    help = 'Drop all objects in database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f'Deleting all objects in database'))

        ToDoList.objects.all().delete()
        ToDo.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'All objects deleted'))

