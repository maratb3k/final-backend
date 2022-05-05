from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Book, Author, Category
from api.serializers import BookSerializer, AuthorSerializer, CategorySerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     # serializer_class = BookSerializer
#     def list(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         pass

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# class BookDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = BookSerializer
#     def get_queryset(self):
#         user = self.request.user
#         books = Book.objects.filter(which_book=self.kwargs['book_id'])
#         return books

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()