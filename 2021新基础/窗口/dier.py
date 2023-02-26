import tkinter as tk
root=tk.Tk()
root.title('王凯旋')
root.geometry('200*200')
def insert_point
e=tk.Entry(root,show='*')
e.pack()
b1=tk.Button(root,text='insert point',width=15,height=2,command=insert_point) #定义按钮
b1.pack()



root.mainloop()
