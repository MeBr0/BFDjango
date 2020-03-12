from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('bookstore.auth_.urls')),
    path('', include('bookstore.books.urls')),

]
