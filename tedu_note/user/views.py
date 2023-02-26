from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
#优化一 引入hash 库
import hashlib

def reg_view(request):
    #注册使用的视图函数
    #GET返回页面
    #POST 提交处理数据
    #1，两次密码要保持一致
    #2，当前用户名是否可用
    #3，插入数据 明文处理密码
    if request.method=='GET':
        # GET 返回页面
        return render(request,'user/register.html')
    elif request.method=='POST':
        username=request.POST['username']
        password_1=request.POST['password_1']
        password_2=request.POST['password_2']
        #判断两次密码输入时候一致
        if password_1 !=password_2:
            return HttpResponse('两次输入的密码不正确')

        #哈希算法 - 给定明文 计算出一段定长的，不可逆的值；然后将该hash值存储到数据库中
        #特点 1，定长输出：不管明文输出多长，hash值都是定长的，比如md5
        #2， 不可逆：无法反向计算出 对应的明文
        #3， 雪崩效应：输入改变，输出必然改变
        m=hashlib.md5() #生成一个md5的计算对象
        m.update(password_2.encode()) #将str字符串转化为字节串
        password_m=m.hexdigest() #拿到字节串的hash值的结果

        #根据post提交过来的username 判断数据库中时候已经有这个用户
        user=User.objects.filter(username=username)
        if user:
            return HttpResponse('用户名已存在，请你用其他用户名')

        #向数据库中插入数据 解决唯一索引 并发插入数据报错问题
        try:
            user=User.objects.create(username=username,password=password_m) #将hash值传进来的值存储到数据库中
        except Exception as e:
            print(f'插入数据报错{e}')
            return HttpResponse('用户名已注册')

        #免登录一天 需要在settings.py文件中把sessions默认保存时间设置为1天
        request.session['username']=user.username
        request.session['uid']=user.id


        return HttpResponse('注册成功')



def login_view(request):
    if request.method=='GET':
        #获取登录页面
        #检查登录状态，如果登录了 显示已登录
        #检查session
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponse('已登录')
        #检查cookies
        c_username=request.COOKIES.get('uname')
        c_uid=request.COOKIES.get('uid')
        if c_username and c_uid:
            #回写session
            request.session['username']=c_username
            request.session['uid']=c_uid
            return HttpResponse('已登录')
        #如果session 和cookies都为空就直接给用户返回登录页面
        return render(request,'user/login.html')

    if request.method=='POST':
        #去除post提交过来的用户名和密码
        username=request.POST['username']
        password=request.POST['password']

        #查询用户名是否存在
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            print(f'用户登录时查询账号时报错{e}')
            return HttpResponse('用户名或者密码不正确')

        #比对密码
        m=hashlib.md5()  #生成md5的计算对象
        m.update(password.encode())  #将str字符串 转化为字节串
        password=m.hexdigest()      #拿到字节串的hash值结果

        if password !=user.password: #和数据库中存储的密码对比
            return HttpResponse('密码错误')

        #启用session 记录会话状态
        request.session['username']=username
        request.session['uid']=user.id

        #如果用户勾选了记住用户名 就给用户添加cookies
        resp=HttpResponse('登录成功') #设置cookies不能像session一样设置在request中 而是要设置在不response中
        remember=request.POST.get('remember')
        print(remember)
        if remember:
            #设置cookies存储时间为三天
            resp.set_cookie('uname',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)

        return resp



