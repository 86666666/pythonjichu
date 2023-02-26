from django.urls import path
#第一种引入视图函数的办法 绝对路径引入
#from mysite3.music.views import * #将应用music 的视图文件中的所有视图函数导入进来
#第二种办法相对路径引入
from .views import *

urlpatterns=[
    #http://127.0.0.1:8001/music/index
    path('index',index_view)

]
