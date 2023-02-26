import os
import subprocess
import time
zongjie=[]   #空列表存储每个命令执行的结果方便最后一次性展示
print('安装tomcat脚本开始运行了')

while True:
    a=input('请您输入 yes 来运行程序，如果您输入结果不正确程序将不执行:')
    if a=="yes":
        print('脚本开始执行')
        break
    else:
        print('你输入的不争取请您继续输入')

a1='sudo apt update'      #linux命令  sudo apt update
a2='apt-get -y upgrade '  #安装软件更新
a3='sudo apt install -y openjdk-11-jdk'  #安装OpenJDK 11 JDK 软件包
a4='java -version '       #安装成功后查看java版本
#a5='java'                 #输入java命令测试安装效果
#a6='wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.62/bin/apache-tomcat-9.0.62.tar.gz'  #下载tomcat安装包，这一步很慢我直接下载好之后上传
a7='tar -axvf /home/wangkaixuan/apache-tomcat-9.0.62.tar.gz'       #解压tomcat 包
a8='mv apache-tomcat-9.0.62 tomcat '                               #重命名
a9='chmod 777 -R /home/wangkaixuan/tomcat/bin'                     #给tomcat/bin目录下的文件赋予可读可写可执行的权限
a10='useradd -U -d /home/wangkaixuan/tomcat/  -s /bin/bash tomcat' #创建一个根目录为/home/wangkaixuan/tomcat 所属用户组为tomcat的tomcat用户
a11='sudo chown -R tomcat: /'                            #修改目录归属到用户和用户组
a12='/home/wangkaixuan/tomcat/bin/startup.sh'                      #开启tomcat
a13='ps -ef | grep tomcat'                                         #通过进程管理命令查看tomcat服务运行状态
a14='cp 1.txt /etc/systemd/system/tomcat.service'                  #将昨天写好的tomcat配置文件写入到1.txt中复制为tomcat 的systemct单元文件
a15='systemctl daemon-reload'                                      #重新加载所有修改过的配置文件
a16='systemctl stop tomcat.service'                                #关闭tomcat服务
a17='systemctl enable tomcat.service'                              #设置tomcat开机自启
a18='systemctl reload tomcat.service'                              #重新加载tomcat配置文件
a19='systemctl status tomcat.service'                              #查看tomcat服务状态





def minlin(a):      #设置一个函数执行重复的操作
    global zongjie
    print('\033[5;31m' + a + ' 正在执行 请稍后\033[0m')
    jieguo=subprocess.getstatusoutput(a)
    os.system('clear')    #linux 清屏命令为clear
    for i in range(20):
        print('--------------')
    if jieguo[0]==0:
        print('\033[1;32m'+a+'命令执行成功\033[0m')
        jieguo1='\033[1;32m'+a+'   命令执行成功\033[0m'  #执行成功的命令保存到变量中 下一步添加到列表中
        print('执行结果是')
        print('\033[1;32m'+jieguo[1]+'\033[om')      #执行成功的命令添加到列表中
        zongjie.append(jieguo1)
    else:
        print('\033[1;31m'+a+'命令执行失败\033[0m')
        jieguo2='\033[1;31m'+a+'   命令执行失败\033[0m'
        zongjie.append(jieguo2)
    in2=input('输入  y 或者 yes 继续')

#sczj 函数作用：将脚本所有命令的执行结果反馈
def sczj():
    for j in range(8):
        print('-------------------------------------------------------------------------')
    print('***********************下面是脚本所有命令的执行结果反馈**************************************')
    for i in zongjie:    #循环打印本脚本所有命令执行结果
        print(i)
        time.sleep(2)
    print('-*-*-*-*-*-*-*-*-*程序到此结束*-*-*-*-*-*-*-*-*-*-*')

# def xieru():  #创建文件的函数
#     with open('~/.vimrc','w')as pd:
#         pd.write('filetype plugin on\n')
#         pd.write("'let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict\n'")

minlin(a1)
minlin(a2)
minlin(a3)
minlin(a4)
# minlin(a5)
# minlin(a6)
minlin(a7)
minlin(a8)
minlin(a9)
minlin(a10)
minlin(a11)
minlin(a12)
minlin(a13)
minlin(a14)
minlin(a15)
minlin(a16)
minlin(a17)
minlin(a18)
minlin(a19)
sczj()

