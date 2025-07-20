from django import forms
from .models import Book,Review

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

class Review_Form(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
        required=True,
        label='Rating'
    )

    class Meta:
        model = Review
        fields = ['content', 'rating']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Review is required.")
        return content

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating:
            raise forms.ValidationError("Rating is required.")
        return rating
