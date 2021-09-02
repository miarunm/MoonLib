from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('rating', 'quote', 'prizes', )