from catalogo.serializers import BookSerializer
from catalogo.models import Book
from rest_framework import viewsets



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
