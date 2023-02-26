import socket
#买手机
iphone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#类通过实例化传参得到一个实例对象，就是一个套接字对象

#绑定手机卡
iphone.bind(('127.0.0.1',8080))#127.0.0.1是本地回环接口用于测试用的

#开机 并监听
iphone.listen(5)#开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
print('开始监听')

# res=iphone.accept()#建立连接
# print('已成功建立连接')


while 1:
    con,address = iphone.accept()# 建立连接
    print('已成功建立连接,客户端的IP地址是：'+str(address))
    con1=con.recv(1024)
    con2=con1.decode()
    con.send('客户端已经收到'.encode('utf-8'),con1)#给客户端发送服务端已经收到消息后的确认消息
    if con1=='客户端要中断连接':
        print('服务端允许客户端中断连接')
        break
con.close()
iphone.close()







