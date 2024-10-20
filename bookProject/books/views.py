from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookFind(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            book = Book.objects.filter(title_icontains=title)

        else:
            book = Book.objects.all()

        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)