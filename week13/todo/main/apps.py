from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'todo.main'

    def ready(self):
        import todo.main.singals
