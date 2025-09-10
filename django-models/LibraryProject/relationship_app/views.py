from django.views.generic import DetailView
from django.shortcuts import render
from .models import Author, Book, Library, Librarian

def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books, 'authors': authors})

class LibraryView(DetailView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()