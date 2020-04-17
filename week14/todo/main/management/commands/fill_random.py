import random

from django.core.management import BaseCommand

from todo.auth_.models import MyUser
from todo.main.models import ToDoList, ToDo


class Command(BaseCommand):
    """
    Creates random object in databases, before it optionally drop database
    """

    help = 'Create random lists and todo elements'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--owner', type=int, help='Id of owner of lists')
        parser.add_argument('-d', '--drop', action='store_true', help='Flag if drop all before creating objects')

    def handle(self, *args, **options):

        owner_id = options.get('owner')
        try:
            owner = MyUser.objects.get(id=owner_id)
        except:
            self.stdout.write(self.style.ERROR(f'User with id {owner_id} now found'))
            return

        if options.get('drop'):
            ToDoList.objects.all().delete()
            ToDo.objects.all().delete()

            self.stdout.write(self.style.WARNING(f'All Todo list and todo objects dropped'))

        list_count = random.randint(1, 10)
        todo_count = random.randint(1, 20)
        lists = []

        # Create lists
        for i in range(list_count):
            listt = ToDoList.objects.create(name=f'list {i}', owner=owner)

            lists.append(listt)

            self.stdout.write(self.style.SUCCESS(f'Todo list {listt.id} created'))

        # Create todos
        for i in range(todo_count):
            listt = lists[random.randint(0, list_count - 1)]
            item = ToDo.objects.create(name=f'todo {i}', list=listt, notes=f'notes {i}')

            self.stdout.write(self.style.SUCCESS(f'Todo item {item.id} created on list {listt.id}'))

