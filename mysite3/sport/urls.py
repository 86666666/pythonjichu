from django.urls import path,include
from .views import index_views

urlpatterns=[
    path('index',index_views)
]