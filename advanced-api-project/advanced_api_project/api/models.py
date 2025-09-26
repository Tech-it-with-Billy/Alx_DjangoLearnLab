from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20)
    publication_year = models.IntegerField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    