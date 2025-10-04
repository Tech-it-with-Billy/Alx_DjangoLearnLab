from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes validation to prevent future publication years.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model fields.
    Includes nested serialization of related books.
    The 'books' field uses BookSerializer for all related Book objects.
    """
    books = BookSerializer(many=True, read_only= True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] 