"""
URL configuration for collegeinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from teacherinfo.views import landing

from teacherinfo.views import login, register,registerinfo

from teacherinfo. views  import dashboard
from teacherinfo.views import registration
from teacherinfo.views import dashboard
from teacherinfo.views import register
from teacherinfo.views import registerinfo
from teacherinfo.views import login
from teacherinfo.views import home,department,settings,faculty

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('registerinfo/', registerinfo, name='registerinfo'),
    path('registration/', registration, name='registration'),
    path('dashboard/',dashboard,name='dashboard'),
    path('faculty/',faculty,name='faculty'),
    path('settings/',settings,name='settings'),
    path('home/',home,name='home'),
    path('department/',department,name='department'),
]

