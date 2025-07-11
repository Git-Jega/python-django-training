from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_date', 'author', 'rating', 'copies']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title.strip()) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 0 or rating > 5):
            raise forms.ValidationError("Rating must be between 0 and 5.")
        return rating

    def clean_copies(self):
        copies = self.cleaned_data.get('copies')
        if copies is not None and copies < 0:
            raise forms.ValidationError("Copies cannot be negative.")
        return copies
