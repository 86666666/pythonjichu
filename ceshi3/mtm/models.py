from django.db import models

class Author(models.Model):
    name=models.CharField('作者',max_length=11)

class BOOK(models.Model):
    title=models.CharField('书名',max_length=11)
    authors=models.ManyToManyField(Author)

# Create your models here
