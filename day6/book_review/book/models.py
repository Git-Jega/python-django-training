from django.db import models
from django.contrib import admin

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    publication_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True) 
    copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    @admin.display(boolean=True,description="Book Availabilty")
    def is_available(self):
        return True if self.copies>0 else False
