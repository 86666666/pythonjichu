from django.shortcuts import render
from django.http import HttpResponse

def index_views(request):
    return HttpResponse('这个是 sport  app')
    pass
# Create your views here.
