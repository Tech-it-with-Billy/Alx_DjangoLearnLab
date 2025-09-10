from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', views.Admin, name='Admin'),
    path('librarian-dashboard/', views.Librarian, name='Librarian'),
    path('member-dashboard/', views.Member, name='Member'),
]