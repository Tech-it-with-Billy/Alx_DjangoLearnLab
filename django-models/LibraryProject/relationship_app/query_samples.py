from models import Author, Book, Library, Librarian
from django.db.models import Q

def books_by_author(author):
    author = Author.objects.get(author=author)
    return Book.objects.filter(author=author)    

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian