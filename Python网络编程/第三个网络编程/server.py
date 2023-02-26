import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #构造类对象
print('s=',s)
print('s的类型是',type(s))
print('本机的主机名是',socket.gethostname())
s.connect(('www.baidu.com',80))
print('s=',s)
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')#构造简单get请求
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()  #关闭连接
data=b''.join(buffer)  #将buffer内所有的元素合并成为一个新的字符串。
hearder,html=data.split(b'\r\n\r\n',1)
print(hearder.decode('utf-8')) #输出报文头部
with open('baidu.html','wb') as f:
    f.write(html)
