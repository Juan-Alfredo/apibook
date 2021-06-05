from catalogo.models import Author
from django.forms import fields
from catalogo.models import Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'nationality', 'genere']

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'editorial', 'year', 'volumen', 'author']