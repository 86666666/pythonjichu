import telnetlib
import time
host='127.0.0.1'
password='19910945'
tn=telnetlib.Telnet(host=host,port=2000,timeout=10)
print('连接成功')
tn.write(b"\n")
tn.read_until(b'') #表示读取到括号内信息为止 b表示将Python中默认的unicode编码变为bytes
# tn.write(b"password.encode('ascii')")
# tn.write(b'\n')
tn.write(b'undo vlan batch 2 3'+b'\n') #
tn.read_until(b'[Y/N]:')
tn.write(b'y')
print('删除vlan成功')
tn.write(b'dis cu \n')#显示程序的当前配置
time.sleep(2)
print(tn.read_very_eager().decode('ascii'))
tn.close() #关闭连接
print('程序执行完毕')
