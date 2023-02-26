f=open('name_list.txt','at',encoding='utf-8')
f.write('wangkaixuan是天才\n')
f.write('张广才是笨蛋\n')
f.close()
q=open('name_list.txt','rt',encoding='utf-8')
q1=q.readlines()
print(q1)
for i in q1:
    print(i.strip('\n'))
q.close()

print('间隔符'.center(68,'-'))
q2=open('name_list.txt','rt',encoding='utf-8')
for i in q2:
    print(i,end='')
q2.close()