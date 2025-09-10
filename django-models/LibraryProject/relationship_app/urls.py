from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', SignUpView.as_view(template_name= 'templates/relationship_app/register.html'), name='SignUp'),
    path('login/', LoginView.as_view(template_name= 'templates/relationship_app/login.html'), name='Login'),
    path('logout/', LogoutView.as_view(template_name= 'templates/relationship_app/logout.html'), name='Logout'),
]
