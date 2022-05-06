## Bookmania
Online store, where you can browse books by category, author and buy them.


### Class diagram
![myapp_models](https://user-images.githubusercontent.com/60798717/167092203-52a15ecd-e6fe-4755-9138-a2484320c28c.png)


#### Models: 
- Person
  - Seller
  - Buyer
- Book
- Author
- Category
- User


#### Serializers:
- AuthorSerializer
- AuthorDetailSerializer
- CategorySerializer
- BookSerializer
- BookDetailSerializer
- BookSeriesSerializer
- PersonSerializer
- BuyerSerializer
- SellerSerializer
- UserSerializer

#### Views:
Views are Class and function based:

CBV:
- AuthorListAPIView
- AuthorDetailAPIView
- CategoryListAPIView
- CategoryDetailAPIView
- BookListAPIView

FBV:
- authors_list
- author_detail
- books_list
- sign_up
- get_user

#### URLS:
- 'authors/' - to get authors list
- 'authors/<int:author_id>/' - to get detail about certain author by id
- 'genres/' - to get list of genres
- 'genres/<int:category_id>' - to get more detail about genres
- 'authors/<int:author_id>/books', views_w12.author_books
    path('genres/<int:category_id>/', views_w12.genre_books
- 'books/' - to get list of books
- 'signup/' - for sign up
- 'users/<str:username>/' - to get detail about user



