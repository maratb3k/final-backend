from django.contrib import admin

# Register your models here.

from api.models import Author, Book, Category, Buyer, Seller, SerieOfBook

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(SerieOfBook)
