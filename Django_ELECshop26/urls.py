from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


'''
创建虚拟环境: pip freeze >shop.txt(批量导出)
             pip install -r shop.txt
'''