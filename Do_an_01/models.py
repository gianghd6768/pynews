from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    content = RichTextUploadingField(blank=True)
    public_day = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='Do_an_01/img', default='Do_an_01/img/logo.jpg')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    submit_day = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.subject

class Subcribe(models.Model):
    email = models.CharField(max_length=254)
    subcribe_day = models.DateField()

class Comment(models.Model):
    post = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    content = RichTextUploadingField(blank=True)
    public_day = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='Do_an_01/img', default='Do_an_01/img/logo.jpg')

    def __str__(self):
        return self.name