from django.db import models

from todo.auth_.models import MyUser


# It is very stupid thing, but example for model inheritance and abstract methods
class NameableModel(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    @property
    def short_name(self):
        raise NotImplementedError()


class ToDoListManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)


class ToDoList(NameableModel):

    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo lists'

    def __str__(self):
        return f'{self.name} todo list'

    @property
    def short_name(self):
        return self.name[:10]

    @classmethod
    def count(cls):
        return cls.objects.count()


class ToDo(NameableModel):

    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    notes = models.CharField(max_length=255, default='', blank=True)
    attachment = models.FileField(upload_to='attachments', null=True, blank=True)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'Todo item'
        verbose_name_plural = 'Todo items'

    def __str__(self):
        return f'{self.name}, in {self.list}'

    @property
    def short_name(self):
        return self.name[:10]

    @property
    def string_is_done(self):
        if self.is_done:
            return 'done'

        return 'not done'

    @classmethod
    def count(cls):
        return cls.objects.count()
