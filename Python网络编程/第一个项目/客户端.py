import socket
#买手机
iphone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#类通过实例化传参得到一个实例对象，就是一个套接字对象


#拨号
iphone.connect(('127.0.0.1',8080))#127.0.0.1是本地回环接口用于测试用的

#收发消息
#iphone.send('hello'.encode("utf-8"))
iphone.send('王凯旋'.encode('utf-8'))
data=iphone.recv(9216)
print(data)

#关闭套接字
iphone.close()