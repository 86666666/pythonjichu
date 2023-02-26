from django.urls import path,include
from .views import *

urlpatterns = [
    path('set/',set_cookies),
    path('get_cookie/',get_cookies),
    path('delete_cookie/',delete_cookies),
    path('set_session/',set_session),
    path('get_session/',get_session)
]
