from django.shortcuts import render
from django.http import *
from .models import *


def all_book(request):
    #过滤 只查询  is_active=True
    all_book = BOOK.objects.filter(is_active=True)
    return render(request, 'all_book.html', locals())


def update_book(request,book_id):
    try:
        book = BOOK.objects.get(id=book_id,is_active=True)#过滤 添加条件  is_active=True
        print(book)
    except:
        print('无法查询')
        return HttpResponse('没有查询到这本书')
    if request.method == 'GET': #如果是get请求 就返回 查询所有数据的 update_book.html
        return render(request, 'update_book.html', locals())
    elif request.method == 'POST':
        book.price=request.POST['price'] #如果是post请求 就将post中  price 和 market_price 所对应的值取出来
        book.market_price=request.POST['market_price']
        book.save()
        return HttpResponseRedirect('/bookstore/all_book/') #修改完之后重定向到 update_book.html 页面
        #return render(request,'all_book.html',locals())


def delete_book(request):
    #通过获取查询字符串 book_id 拿到要删除的book的id
    book_id=request.GET.get('book_id')
    if not book_id: #如果没有bookid 返回页面查询异常
        return HttpResponse('请求异常')
    try:
        book=BOOK.objects.get(id=book_id,is_active=True)
    except:
        return HttpResponse('没有查到数据')
    #将其is_active 改为False
    book.is_active=False
    book.save()
    #302 跳转回all_book
    return HttpResponseRedirect('/bookstore/all_book/')

# Create your views here.
