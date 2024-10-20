from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
# Create your views here.

class BookCreate(generics.CreateAPIView):
    model = Book
    serializer_class = BookSerializer