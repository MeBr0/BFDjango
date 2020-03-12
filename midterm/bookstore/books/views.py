from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from bookstore.books.models import Book, Journal
from bookstore.books.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allows change information only for super admins
    def get_permissions(self):
        if self.request.method == 'GET':
            return IsAuthenticated(),

        else:
            return IsSuperAdmin(),


class JournalViewSet(viewsets.ModelViewSet):

    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    # Allows change information only for super admins
    def get_permissions(self):
        if self.request.method == 'GET':
            return IsAuthenticated(),

        else:
            return IsSuperAdmin(),


# Permission that allows pass only for users with is_super_admin == True
class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_super_admin
