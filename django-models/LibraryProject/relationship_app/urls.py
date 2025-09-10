from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', SignUpView.as_view(), name='templates/relationship_app/signup'),
    path('Login/', LoginView.as_view(), name='templates/relationship_app/login'),
    path('Logout/', LogoutView.as_view(), name='templates/relationship_app/logout'),
]
