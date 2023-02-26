from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
# Create your views here.
import random


def indexApi(request):
    a=random.randint(0,99)
    return JsonResponse({"code":200,"msg":"ok","data":"这是第"+str(a)+"次数据啊"})


def index(request):
    return render(request,"test.html")
