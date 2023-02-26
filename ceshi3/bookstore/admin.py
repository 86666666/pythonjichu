from django.contrib import admin
from .models import BOOK #导入models.py文件中定义的BOOK类
# Register your models here.
class BOOKManager(admin.ModelAdmin):
    #list_display 列表页显示哪些字段
    list_display=['id','title','price','market_price','pub'] #定义列表要显示的字段信息
    #控制list_display中的字段，哪些可以链接到修改页面
    list_display_links = ['title'] #设置点击titile可以链接到修改页面
    #添加过滤器
    list_filter = ['pub']
    #添加搜索框 ['模糊查询']
    search_fields = ['pub','title'] #将列表页中的 pub title字段设置为可以在搜索框中进行模糊查找的两个字段
    #添加可以在列表页编辑的字段
    list_editable = ['pub']  #将列表页的出版社设置为可编辑

admin.site.register(BOOK,BOOKManager)  #注册我们自定义的模型类 2，绑定模型类与管理器类

from .models import Author #引入Author类
class AuthorManager():
    pass
