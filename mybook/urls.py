from django.urls import path,include
from . import views
from rest_framework import routers
from .views import AuthorViewSet, mybookViewSet

app_name = 'mybook'
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'mybooks', mybookViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/add/', views.add_book, name='add_book'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/add/', views.add_author, name='add_author'),
    path('api2/', include(router.urls)),
     
]
