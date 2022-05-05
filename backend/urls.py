from django.contrib import admin
from django.urls import path, include
from api.views.viewSet import BookViewSet, AuthorViewSet, CategoryViewSet
# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'api', viewSet.BookViewSet)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'booksList', BookViewSet, basename="books")
router.register(r'authorsList', AuthorViewSet, basename="authors")
router.register(r'categoryList', CategoryViewSet, basename="categories")

# router.register(r'bookList/<int:book_id>', BookDetailViewSet, basename="book")
#router.register(r'bookList/1/)', BookDetailViewSet, basename="book")

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(urlpatterns))
    path('api/', include('api.urls'))

]
