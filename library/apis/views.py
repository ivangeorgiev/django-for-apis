from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
