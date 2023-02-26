from django.shortcuts import render
from django.http import HttpResponse

#设置cookies
def set_cookies(request):
    resp=HttpResponse('SET COOKIES IS OK') #将返回的response对象存储到变量中
    resp.set_cookie('uname','ui',500)   #response 使用set_cookie方法通过键值对的方式设置cookies
    return resp  #最后将response对象返回

#获取cookies
def get_cookies(request):
    resp1=request.COOKIES.get('uname','null') #获取浏览器发送过来的cookies
    return HttpResponse(f'cookies is {resp1}')  #将取得的cookie 返回到页面上

#删除cookies
def delete_cookies(request):
    resp=HttpResponse('COOKIE IS DELETE')
    resp.delete_cookie('uname')
    return resp


#设置session

def set_session(request):
    request.session['ceshi']='wc'
    return HttpResponse('SET SESSION IS OK ')

#获取session
def get_session(request):
    value=request.session['ceshi']
    return HttpResponse(f'session is {value}')
# Create your views here.
