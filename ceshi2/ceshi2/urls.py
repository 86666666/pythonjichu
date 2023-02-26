from django.contrib import admin
from django.urls import path
from .views import *  #修改导入了所有函数
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/url',test_url,name='base_index'),
#使用了path函数的name属性为反向解析做铺垫
#增加难度使用了path转换器 相应的视图函数中也要修改
    path('test_url_result/<int:age>',test_url_result,name='tr')
]
