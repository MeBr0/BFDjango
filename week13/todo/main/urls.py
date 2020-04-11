from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import ListViewSet, TaskViewSet

router = ExtendedSimpleRouter()

(
    router.register(r'', ListViewSet, basename='list')
        .register(r'todo', TaskViewSet, basename='list-task', parents_query_lookups=['list'])
)

urlpatterns = router.urls
