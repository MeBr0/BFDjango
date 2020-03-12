from rest_framework.routers import DefaultRouter

from BookStore.books.views import BookViewSet, JournalViewSet

router = DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'journals', JournalViewSet)

urlpatterns = router.urls
