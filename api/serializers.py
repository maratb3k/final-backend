from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import  Author, Category, Book, BookSeries, SerieOfBook, Seller, Buyer

# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     biography = serializers.CharField()
#     image = serializers.CharField()
#
#     def create(self, validated_data):
#         author = Author.objects.create(name=validated_data.get('name', 'biography', 'image'))
#         return author
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.save()
#         return instance

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image = serializers.CharField()

    class Meta:
        model = Author
        fields = ('id', 'name', 'image')


class AuthorDetailSerializer(AuthorSerializer):
    biography = serializers.CharField()
    years_of_life = serializers.DateField()
    genres = serializers.ListField(
       child=serializers.CharField()
    )

    class Meta:
        model = Author
        fields = ('id', 'name', 'biography', 'image', 'years_of_life', 'genres')



class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    category = serializers.CharField()

    def create(self, validated_data):
        book = Book.objects.create(name=validated_data.get('name', 'author', 'category'))
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance


class BookDetailSerializer(BookSerializer):
    year = serializers.IntegerField()
    description = serializers.CharField()
    image = serializers.CharField()
    seller = serializers.CharField()
    likes = serializers.IntegerField()

    # def create(self, validated_data):
    #     book = Book.objects.create(name=validated_data.get('name', 'author', 'category', 'year', 'description', 'image', 'likes', seller))
    #     return book
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class BookSeriesSerializer(serializers.ModelSerializer):
    series = BookSerializer(many=True, read_only=True)

    class Meta:
        model = SerieOfBook
        fields = ['name', 'author', 'series']

# class BookSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Book
#         fields = ('id', 'name', 'author', 'genre', 'year', 'description', 'likes', 'image')

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=150)
#     # first_name = serializers.CharField(max_length=30)
#     # last_name = serializers.CharField(max_length=150)
#     email = serializers.CharField(max_length=254)
#     password = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         user = User.objects.create_user(username=validated_data.get('username'),
#                                         email=validated_data.get('email'),
#                                         password=validated_data.get('password'))
#         # user.first_name = validated_data.get('first_name')
#         # user.last_name = validated_data.get('last_name')
#         user.save()
#         return user
#
#     def update(self, instance, validated_data):
#         return instance

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    date_of_birth = serializers.DateField()
    date_of_joining = serializers.DateField()
    email = serializers.CharField()
    password = serializers.CharField()
    role = serializers.CharField()
    image = serializers.CharField()

class BuyerSerializer(PersonSerializer):
    address = serializers.CharField()

    def create(self, validated_data):
        buyer = Buyer.objects.create(name=validated_data.get('name', 'date_of_birth', 'date_of_joining', 'email', 'password', 'role', 'image', 'address'))
        return buyer

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance




class SellerSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()

    def create(self, validated_data):
        seller = Seller.objects.create(name=validated_data.get('name', 'date_of_birth', 'date_of_joining', 'email', 'password', 'role', 'image', 'rating'))
        return seller

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


