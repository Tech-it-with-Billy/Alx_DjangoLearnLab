from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book 
from .serializers import BookSerializer
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter

class ListView(generics.ListAPIView):
    """
    Return a list of books
    GET /api/books/
    """
    queryset = Book.object.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class DetailView(generics.RetrieveAPIView):
    """
    Returns a specific book by ID.
    GET /api/book/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class CreateView(generics.CreateAPIView):
    """
    Create new book
    POST /api/books/create/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, serializer):
        serializer.save(created_by= self.request.user)

class UpdateView(generics.UpdateAPIView):
    """
    Update a book
    PUT/PATCH /api/books/<id>/update/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def update(self, serializer):
        serializer.save(update_by= self.request.user)

class DeleteView(generics.DestroyAPIView):
    """
    Delete a book record
    DELETE /api/books/<id>/delete/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
