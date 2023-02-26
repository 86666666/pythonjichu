
from django.contrib import admin
from django.urls import path,include
 #将index 的视图函数 引入进来


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),#引入分布式路由
    path('index/',include('index.urls'))
]
