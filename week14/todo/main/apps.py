from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'todo.main'

    # Register signals
    def ready(self):
        import todo.main.singals
