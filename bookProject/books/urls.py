from django.urls import path
from .views import BookCreate

urlpatterns = [
    path('create/', BookCreate.as_view(), name='book-create'),
]