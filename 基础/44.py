# #python函数定义时可已预先为部分参数设置默认值好处是调用函数的时候不用再提供参数的实际值
# # def fun(a,b=1,c=2):
# #     print(a,b,c)
# #
# # fun(0)
# # fun(1,2)
# # fun(1,2,3)
# print('你可是\'一个大笨\'蛋啊')
# print('王凯旋可是一个大天才呢\n\'王凯旋可真是一个大天才呢\'')
# print('王凯旋可是一个天才啊')
# print('你是不是一个大笨蛋你自己说说，我早就收你是一个大笨蛋了')
# print('没想到你还是一个大笨蛋啊，\n我真的是看错你了，都怪老子太笨了，哈哈哈原来你即使那个大笨蛋啊，哈哈哈哈原来如此，')
# def fun(a,b=4,c=3):
#     print(a+b+c)
#     return a+b+c
#
#
# fun(5)
# a4=fun(5)
# #print(a4)


# def func():
#     while True:
#         h=int(input('请输入小时'))
#         if h<0 or h>24:
#             raise Exception('您输入的小时不正确')
#         m=int(input('请输入分钟'))
#         if m<0 or h>60:
#             raise Exception('您输入的分钟不正确')
#         s=int(input('请输入当前的秒'))
#         if s<0 or s>60:
#             raise Exception('您输入的秒不正确')
#         m1=(h,'是',m,'分',s,'秒')
#         break
#     return m1
#
# try:
#     func()
# except Exception as err:
#     print(err)
# import mokuia        #导入整个mokuia模块
# print(mokuia.mymin(9,89))
# print(mokuia.mymax(234,2424))
#
#
# from mokuia import mymin as np #导入mokuia 模块 中的mymin函数 重命名为np
# print(np(99,90))

s=
