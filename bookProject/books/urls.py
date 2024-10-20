from django.urls import path
from .views import BookCreate, BookRetrieveUpdateDestroy, BookFind

urlpatterns = [
    path('book/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>', BookRetrieveUpdateDestroy.as_view(), name='book-update'),
    path('booksearch/', BookFind.as_view(), name='book-search'),
]