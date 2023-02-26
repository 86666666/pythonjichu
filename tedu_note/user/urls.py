from django.urls import path, include
from .views import *


urlpatterns=[
    path('reg/',reg_view),
    path('login/',login_view)
]