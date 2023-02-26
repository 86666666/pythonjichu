from django.db import models

class Publisher(models.Model):
    name=models.CharField('出版社名称',max_length=50)
    #出版社 一


class BOOK(models.Model):
    title=models.CharField('书名',max_length=11)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    #书名  多
# Create your models here.
