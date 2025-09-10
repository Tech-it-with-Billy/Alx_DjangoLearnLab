from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books.as_view(), name='list_books'),
    path('library/', views.library_detail.as_view(), name='library_detail'),
]
