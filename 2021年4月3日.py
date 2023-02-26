st=[]
def getstudent():
    global st
    st=[]
    st.append({'name':'张三','gender':'男','age':20})
    st.append({'name':'李四','gender':'女','age':12})
    st.append({'name':'王五','gender':'男','age':23})

def bianli(name):
    for i in st:
        print(i)
        if i['name']==name:
            print(i['name'],i['gender'],i['age'])
            break
    print('没有这个学生')
    return




getstudent()
bianli('王五')
bianli('王凯旋')

