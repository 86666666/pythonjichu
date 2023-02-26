'''
d=("E:\\迅雷下载\pi_digits.txt")
with open(d,encoding='UTF-8')as w:
    for i in w:
        print(i.rstrip())
      
        
c=("C:\\Users\86666\Desktop\自己编写的Python程序\90.txt")
with open(c,encoding='UTF-8')as w:
    c=w.read()
    print(type(c))
    for i in c:
        print(i)
       
d=("E:\\迅雷下载\pi_digits.txt")
with open(d,encoding='UTF-8')as w:
    df=w.read()
    for i in df:
        print(i)   

d=("E:\\迅雷下载\pi_digits.txt")
with open(d,encoding='UTF-8')as w:
    for i in w:
        print(i)

#文件的写入与读出
# 1 写入文件
for i in range(9):
    
    c=("C:\\Users\86666\Desktop\自己编写的Python程序\90.txt")
    with open(c,'a') as io:
        io.write('王凯旋是天才5665565\n')
        io.write('你们信不信王凯旋是天才\n')

# 2 读出文件

c=("C:\\Users\86666\Desktop\自己编写的Python程序\90.txt")
with open(c,) as io:
    io=io.read()
    print(io)

try:
    f=open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','rt',encoding='UTF-8')
    f.read()
    print(f)
except:
    print('文件打开异常')


#教材上的写入文件的例子，没有读出文件的代码
# 1 用只写模式 'wt' 写入文件（清除源文件）
try:
    fj=open('C:\\Users\86666\Desktop\自己编写的Python程序\92.txt','wt')
    fj.write('56abcxy')
    fj.close()
except Exception as err:
    print(err)

# 2 用追加模式  'at'  写入文件续写文件

try:
    fj=open('C:\\Users\86666\Desktop\自己编写的Python程序\92.txt',"at")
    fj.write('\nmore')
    fj.close()
except Exception as err:
    print('写入文件失败')

#文件指针
#1写文件
ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','wt')
ui.write('iopiop')
ui.close()




#2读文件
ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','rt')

print(ui.tell())



#用函数来处理文件
def count_words(filename):
    try:
        with open(filename,'rt') as ui:
            yi=ui.read()
    except Exception as err:
        print(err)
    ji=yi.split()#读出文件的变量不能在函数外使用
    print(len(ji))

filename=('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt')
count_words(filename)







