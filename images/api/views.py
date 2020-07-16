from rest_framework.viewsets import ModelViewSet
from ..models import Book
from .serializers import BookSerializer
from django.http import HttpResponse

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)