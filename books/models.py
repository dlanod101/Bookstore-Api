from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=200, default='Unknown')
    available = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title