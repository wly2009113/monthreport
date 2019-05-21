"""monthreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from load import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #新增一个url，访问load app下的views.py 的load_page 方法
    path('load/',views.load_page)
=======
import fee.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qloudfee/',fee.views.refresh),
>>>>>>> a633854a721c6ac8da141969ab5ef0ef715281c4
]
