from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/',include('music.urls')),
    path('sport/',include('sport.urls')),
    path('news/',include('news.urls'))
]
