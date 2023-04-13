from django.db import models

# Create your models he
class booksinfo(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    book_writer = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/bookImage")