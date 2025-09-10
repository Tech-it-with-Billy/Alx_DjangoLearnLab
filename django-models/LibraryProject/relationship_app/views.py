from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Author, Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books, 'authors': authors})

class library_detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()