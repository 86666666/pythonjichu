from django.http import HttpResponse

def page_2003(request):
    html='<h1>这是一个页面的标签<h1>'
    return HttpResponse(html)

def index_view(request):
    html='<h1>这个是我的首页<h1>'
    return HttpResponse(html)

def page1_view(request):
    html='<h1>这个是第1个页面<h1>'
    return HttpResponse(html)

def page2_view(request):
    html='<h1>这个是第2个页面<h1>'
    return HttpResponse(html)

#path转换器使用的视图函数
def intpg(request,pg):
    html='<h1>这是第'+str(pg)+'个页面<h1>'
    return HttpResponse(html)
#path计算机使用的视图函数
def cal_view(request,n,op,m):
    s=0
    if op not in['add','sub','mul']:
        return HttpResponse('错误：---op的值应该为 add，sub， mul')
    elif op=='add':  #n+m
        s=n+m
    elif op=='sub':  #n-m
        s=n-m
    elif op=='mul':
        s=n*m
    return HttpResponse('结果为%s' % s)







