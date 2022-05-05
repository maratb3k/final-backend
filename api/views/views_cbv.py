from django.forms import forms
from rest_framework.views import APIView
from django.views import View
from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework import status
from api.models import Author, Category, Book
from api.serializers import AuthorSerializer, CategorySerializer, BookSerializer, BookDetailSerializer
from rest_framework.permissions import IsAuthenticated


class AuthorListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AuthorDetailAPIView(APIView):
    def get_object(self, author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist as e:
            raise Http404

    def get(self, request, author_id):
        author = self.get_object(author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def getAuthorBooks(self, request, author_id):
        author = self.get_object(author_id)
        authorBooks = author.book_set.all()
        serializer = BookSerializer(authorBooks)
        return Response(serializer.data)

    def put(self, request, author_id):
        author = self.get_object(author_id)
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, author_id):
        author = self.get_object(author_id)
        author.delete()
        return Response({'message': 'deleted'}, status=204)


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CategoryDetailAPIView(APIView):
    def get_object(self, genre_id):
        try:
            return Category.objects.get(id=genre_id)
        except Category.DoesNotExist as e:
            raise Http404

    def get(self, request, genre_id):
        category = self.get_object(genre_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, genre_id):
        category = self.get_object(genre_id)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, genre_id):
        category = self.get_object(genre_id)
        category.delete()
        return Response({'message': 'deleted'}, status=204)

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)