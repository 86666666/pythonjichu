from django.urls import path,include
from .views import *  #导入视图文件中的所有视图函数

urlpatterns=[
    path('all_book/',all_book),
    path('update_book/<int:book_id>/',update_book),
    path('delete_book',delete_book)
]