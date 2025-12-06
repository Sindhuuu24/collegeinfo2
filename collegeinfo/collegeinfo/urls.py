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
<<<<<<< HEAD
from teacherinfo. views  import dashboard
from teacherinfo.views import register
from teacherinfo.views import registerinfo
=======
<<<<<<< HEAD
<<<<<<< HEAD
from teacherinfo.views import registration
=======
from teacherinfo.views import dashboard
>>>>>>> dashboard
>>>>>>> 349b643d65a5e6f0ab2f65bd4902ca701b7a9315

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
<<<<<<< HEAD
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('registerinfo/', registerinfo, name='registerinfo'),
=======
<<<<<<< HEAD
    path('registration/', registration, name='registration'),
=======
    path('dashboard/',dashboard,name='dashboard'),
>>>>>>> dashboard
=======
from teacherinfo.views import login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
    path('login/', login, name='login'),
>>>>>>> login
>>>>>>> 349b643d65a5e6f0ab2f65bd4902ca701b7a9315
]
