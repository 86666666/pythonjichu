from django.http import HttpResponse,JsonResponse,HttpResponseRedirect #导入响应的重定向子类
#from django.shortcuts import render #导入render
from django.shortcuts import render

def test_static(request):
    return render(request,'test_static.html')
