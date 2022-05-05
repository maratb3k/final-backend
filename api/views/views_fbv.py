import json

from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from rest_framework import status

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Author, Book
from api.serializers import AuthorSerializer, UserSerializer, BookSerializer, BookDetailSerializer, AuthorDetailSerializer


@api_view(['GET', 'POST'])
def authors_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AuthorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist as e:
        return Response({'error': str(e)}, status=400)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        author.delete()
        return Response({'message': 'deleted'}, status=204)

@api_view(['GET', 'POST'])
def books_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)