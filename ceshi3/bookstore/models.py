from django.db import models
class BOOK(models.Model):
    title=models.CharField('书名',max_length=50,default='',unique=True) #书名
    price=models.DecimalField('定价',max_digits=7,decimal_places=2,default=0.0) #价格
    market_price=models.DecimalField('零售价',max_digits=7,decimal_places=2,default=0.0)
    info=models.CharField('信息',max_length=100,default='')# Create your models here.  #信息f
    pub=models.CharField('出版社',max_length=30,default='',) #出版社为非空，django中的null 默认为空
    is_active=models.BooleanField('是否活跃',default=True) #添加字段 标记该记录是否活跃
    class Meta:
        db_table='book1'
        verbose_name='图书'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '%s %s %s %s %s' %(self.title,self.price,self.market_price,self.info,self.pub)

class Author(models.Model):
    name=models.CharField('姓名',max_length=11,default='')#非空
    age=models.IntegerField('年龄',default=1)  #默认值为1
    email=models.EmailField('邮箱',null=True)  #允许为空
    class Meta:
        db_table='author'

