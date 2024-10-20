from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class BookCreate(generics.CreateAPIView):
    """
    -`POST` Creates a new Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    -`GET` Returns a particular existing Book by its id
    -`PUT` Updates an existing Book
    -`PATCH` Partially updates an existing Book
    -`DELETE` Deletes an existing Book
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookFind(APIView):
    """
    -`GET` Returns a Books with specific title but returns all books if no book matches said title
    """
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'title',
                openapi.IN_QUERY,
                description="Returns a Books with specific title but returns all books if no book matches said title",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            book = Book.objects.filter(title__icontains=title)

        else:
            book = Book.objects.all()

        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)