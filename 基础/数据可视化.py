'''
import matplotlib.pylab as pit
aq=[1,4,9,16,25]
pit.plot(aq,linewidth=5)#linewidth线条宽度
pit.show()#（展示方法）打开查看器显示绘制的图形

import json
ji={91:90,'王凯旋在':'北京',90:'习近平'}
j=json.dumps(ji,ensure_ascii=False)
print(j,type(j))
zidian=json.loads(j)
print(zidian,type(zidian))
'''

