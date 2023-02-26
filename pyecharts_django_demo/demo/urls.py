from django.urls import path
from .views import *

urlpatterns=[
    #第一个bar视图
    path('bar',ChartView.as_view(), name='demo'),
    #第二个bar2视图
    path('bar2',ChartView2.as_view(),name='demo'),
    #第三个pie1视图
    path('pie1',ChartView3.as_view(),name='demo'),
    #第四个line1 视图
    path('line1',ChartView4.as_view(),name='demo'),
    path('line2',ChartView5.as_view(),name='demo'),
    path('bar3',ChartView6.as_view(),name='demo'),
    path('index', IndexView.as_view(), name='demo'),
    path('bindex',IndexView2.as_view(),name='demo'),
    path('cindex',IndexView3.as_view(),name='demo')
]
