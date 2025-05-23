from django.urls import path
from .views import BookCreate, BookRetrieveUpdateDestroy, BookFind

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book API",
      default_version='v1',
      description="A simple CRUD Api for an online book store.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=()
)

urlpatterns = [
    path('book/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>', BookRetrieveUpdateDestroy.as_view(), name='book-update'),
    path('booksearch/', BookFind.as_view(), name='book-search'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]