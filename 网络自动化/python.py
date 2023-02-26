import telnetlib
import time
def huoqu():  #获取ip和端口
   global host
   global port
   host=input("请输入要连接的主机ip")
   port=input("请输入端口号")
huoqu()
def lianjie():
    try:
        global tn
        tn=telnetlib.Telnet(host=host,port=port)
        print('连接成功')
    except:
        print('连接失败')
lianjie()
tn.write(b'\n') #回车去除干扰
tn.read_until(b'') #读到回车后产生的空格为止
tn.write(b'gvrp \n')
print('全局启动gvrp成功')
tn.write(b'interface g0/0/1 \n')
print('成功进入接口视图')
tn.write(b'port link-type trunk \n')
tn.write(b'port trunk allow-pass vlan all \n')
tn.write(b'gvrp\n')
print('全局和接口模式gvrp启动成功')
# tn.write(b' \n')
# tn.write(b' \n')
# tn.write(b' \n')
# tn.write(b' \n')

tn.close() #关闭连接

