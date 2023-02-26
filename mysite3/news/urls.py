from django.urls import path,include,re_path
from .views import index_view
urlpatterns=[
    path('index',index_view)
]