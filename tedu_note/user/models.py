from django.db import models

class User(models.Model):
    username=models.CharField('用户名',max_length=30,default='',unique=True)
    password=models.CharField('密码',max_length=32,default='')  #要存储md5的值必须字段长度为32
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    update_time=models.DateTimeField('更新时间',auto_now=True)

    def __str__(self):
        return f'username {self.username}'  #格式化输出打印格式
    pass
# Create your models here.
