from django.urls import path
from main.views import *

urlpatterns = [
    path('', MainPageViews.as_view(), name='index'),
    path('books/<str:slug>', CategoryDetailView.as_view(), name='category'),
    path('books/', CategoryListView.as_view(), name='category_list'),
    path('genres/', genre, name='genres'),
    path('genres/<str:slug>/', GenreDetailView.as_view(), name='genre_detail'),
    path('add-book/', add_book, name='add_book'),
    path('update-book/<int:pk>/', update_book, name='update-book'),
    path('delete-book/<int:pk>/', DeleteBookView.as_view(), name='delete-book'),
    path('book/<str:pk>/', BookDetailView.as_view(), name='book-detail'),
]