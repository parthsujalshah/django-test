from rest_framework.viewsets import ModelViewSet
from ..models import Book
from .serializers import BookSerializer
from django.http import HttpResponse

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer