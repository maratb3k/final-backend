from api.views import views_cbv, views_w12, views_fbv, viewSet
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    # path('authors/', views_cbv.AuthorListAPIView.as_view()),
    # path('authors/<int:author_id>/', views_cbv.AuthorDetailAPIView.as_view()),
    path('authors/', views_fbv.authors_list),
    path('authors/<int:author_id>/', views_fbv.author_detail),

    path('genres/', views_cbv.CategoryListAPIView.as_view()),
    # path('genres/<int:category_id>', views_cbv.CategoryDetailAPIView.as_view()),
    path('authors/<int:author_id>/books', views_w12.author_books),
    path('genres/<int:category_id>/', views_w12.genre_books),
    path('books/', views_fbv.books_list),
    path('signup/', views_fbv.sign_up),
    path('users/<str:username>/', views_fbv.get_user),
    path('books/<int:book_id>/', views_w12.book_detail),
    # path('books/<int:book_id>/books', views_w12.author_books),

]
