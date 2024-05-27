from django import forms
from .models import mybook
from .models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = mybook
        fields = ['title', 'published_date', 'description', 'author']



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']