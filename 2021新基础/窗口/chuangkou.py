import tkinter as tk
root=tk.Tk() #创建一个窗口对象
root.title('wangkaixuan')
#root.geometry('200*100')
var=tk.StringVar() #定义一个字符串变量
i=tk.Label(root,textvariable=var,bg='red',font=('Times',12),width=15,height=2)
i.pack()
on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('你点击了我')
    else:
        on_hit=False
        var.set('')


i2=tk.Button(root,text='点击我',width=15,height=12,command=hit_me)
i2.pack()
root.mainloop()
