from django.http import HttpResponse,JsonResponse,HttpResponseRedirect #导入响应的重定向子类
from django.shortcuts import render #导入render


def test_url(request):
    return render(request,'test_url.html')

def test_url_result(request,age):
    from django.urls import reverse  #引入反向解析函数reverse
    url=reverse('base_index')       #解析路由中别名为base_index的url
    return HttpResponseRedirect(url) #重定向到反向解析出来的url页面
    #return HttpResponse('----test url res is ok')

