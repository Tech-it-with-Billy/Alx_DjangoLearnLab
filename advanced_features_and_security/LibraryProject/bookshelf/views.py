from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms
from django.http import HttpResponse

@permission_required('your_app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('your_app_name.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

@permission_required('your_app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

def secure_response(request):
    response = HttpResponse("This is a secure response")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' cdn.jsdelivr.net"
    return response