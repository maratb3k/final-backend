from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import pre_save,post_save
from django import forms
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    BUYER = "B"
    SELLER = "S"
    ROLE_CHOICES = (
        (BUYER, "Buyer"),
        (SELLER, "Seller")
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="Buyer", null=True, blank=True)
    image = models.CharField(max_length=300, null=True)

    class Meta:
        abstract = True

class Buyer(Person):
    address = models.TextField(null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'date_of_joining': self.date_of_joining,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'image': self.image,
            'address': self.address
        }

    class Meta:
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'


class AuthorManager(models.Manager):
    def create_user(self, id, name, image, **extra_fields):
        if not name:
            raise ValueError('The given username must be set')
        id = self.normalize_id(id)
        name = self.model.normalize_name(name)
        image = self.model.normalize_image(image)
        user = self.model(id=id, username=name, image=image, **extra_fields)
        # user.set_password(password)
        user.save(using=self._db)
        return user


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=300, null=True)
    years_of_life = models.DateField(null=True, blank=True)
    genres = models.TextField(null=True)

    objects = AuthorManager()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'image': self.image,
            'years_of_life':  self.years_of_life
        }

class Seller(Person):
    rating = models.IntegerField(blank=True, null=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'date_of_joining': self.date_of_joining,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'image': self.image,
            'rating': self.rating

        }

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

# class BookManager(models.Manager):
#     def getByYear(self, year):
#         return self.filter(year=year)


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)



class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    year = models.IntegerField()
    likes = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=300, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)

    # objects = BookManager()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.name,
            'genre': self.category.name,
            'year': self.year,
            'description': self.description,
            'likes': self.likes,
            'image': self.image,
            'seller': self.seller
        }

class PublishingHouse(Book):
    nameOfPublishing = models.CharField(max_length=100)

class Country(Book):
    nameOfCountry = models.CharField(max_length=100)

class BookSeries(Book):
    nameOfSeries = models.CharField(max_length=100)

class SerieOfBook(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author
        }

def save_book(sender, instance, **kwargs):
    print("Pre Save for Book")
pre_save.connect(save_book,sender=Book)

def create_book(sender, instance, created, **kwargs):
    if created:
        #Book.objects.create(book=instance)
        print("Book created")
post_save.connect(create_book, sender=Book)

def update_book(sender, instance, created, **kwargs):
    if created == False:
        print("Book Updated")
post_save.connect(update_book, sender=Book)

def create_author(sender, instance, created, **kwargs):
    if created:
        print("Author created")
post_save.connect(create_author, sender=Author)

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.name,
            'password': self.password,
            'email': self.email
        }
