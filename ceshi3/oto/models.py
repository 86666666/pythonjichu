from django.db import models
class Author(models.Model):
    name=models.CharField('作家',max_length=50)


class Wife(models.Model):
    name=models.CharField('妻子',max_length=50)
    author=models.OneToOneField(Author,on_delete=models.CASCADE) #增加一对一属性 设置外键

# Create your models here.
