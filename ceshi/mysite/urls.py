from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *  #导入vies视图

urlpatterns = [
    path('index', index),
    path('indexApi',indexApi)

]