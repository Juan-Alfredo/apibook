from catalogo.models import Author
from catalogo.models import Book
from django import forms
from django.forms.models import ModelForm

class BookForm(forms.Form):
    title = forms.CharField(label='Title:')
    autor=forms.ModelChoiceField(queryset=Author.objects.all())
    editorial=forms.CharField(label='Editorial:')
    year=forms.IntegerField(label='Year:')
    volumen=forms.IntegerField(label='Volumen:')

class ModelBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'editorial', 'year', 'volumen']