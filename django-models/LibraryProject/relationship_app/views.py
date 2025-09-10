from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Author, Book
from .models import Library

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path



def list_books(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    template_name = 'relationship_app/list_books.html'
    return render(request, template_name, {'books': books, 'authors': authors})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/templates/relationship_app/register.html'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
]

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
]

