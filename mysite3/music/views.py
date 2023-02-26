from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return HttpResponse('这个是音乐频道首页')
    pass
# Create your views here.
