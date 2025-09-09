from relationship_app.models import Author, Book, Library, Librarian

# Sample Queries
def book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author_name)

def books_in_library(library_name):
    return Library.objects.filter(name=library_name)

def librarian_of_library(library_name):
    return Librarian.objects.get(name=library_name)