# chat_app/models.py
import uuid
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=100)
    personal_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    publication_date = models.DateField()
    frontal_page = models.ImageField(upload_to='frontal_pages', null=True, blank=True)
    book_file = models.FileField(upload_to='books', null=True, blank=True)

    def __str__(self):
        return str(self.title+" : "+str(self.uid))

class ExtractedBook(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, related_name='extracted_books', on_delete=models.CASCADE,primary_key=True)
    book_file = models.FileField(upload_to='extracted_books', null=True, blank=True)

    def __str__(self):
        return str(self.book.title+" : "+str(self.book))

class Review(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.reviewer_name
    

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    page=models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'