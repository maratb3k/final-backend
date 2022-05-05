from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from api.serializers import AuthorSerializer


# Create your views here.
from api.models import Author, Book, Category
from api.serializers import AuthorSerializer


@csrf_exempt
def authors_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def author_detail(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = AuthorSerializer(instance=author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == "DELETE":
        author.delete()
        return JsonResponse({'message': 'deleted'}, status=204)



def author_books(request, author_id):
    if request.method == "GET":
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        books = author.books_set.all()
        books_json = [b.to_json() for b in books]
        return JsonResponse(books_json, safe=False)


@csrf_exempt
def books_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        books_json = [book.to_json() for book in books]
        return JsonResponse(books_json, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        try:
            book = Book.objects.create(name=data['name'], author=data['author'], year=data['year'],
                                       genre=data['genre'], description=data['description'], likes=data['likes'])
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(book.to_json())


@csrf_exempt
def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == "GET":
        return JsonResponse(book.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        book.name = data['name']
        book.save()
        return JsonResponse(book.to_json())
    elif request.method == "DELETE":
        book.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def author_books(request, author_id):
    if request.method == "GET":
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        books = author.book_set.all()
        books_json = [b.to_json() for b in books]

        return JsonResponse(books_json, safe=False)

@csrf_exempt
def genre_books(request, category_id):
    if request.method == "GET":
        try:
            genre = Category.objects.get(id=category_id)
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        books = genre.book_set.all()
        books_json = [b.to_json() for b in books]

        return JsonResponse(books_json, safe=False)