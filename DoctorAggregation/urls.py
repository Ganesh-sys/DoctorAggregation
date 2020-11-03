"""DoctorAggregation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from HospitalApp.views import *
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    #path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('',Index,name='home'),
    path('login/',Login,name='login'),
    path('logout/',LogOut,name='logout'),
    path('thank/',Thank,name="thank"),
    path('view_doctor/',View_Doctor,name="view_doctor"),
    path('add_doctor/',Add_Doctor,name="add_doctor"),
    path('delete_doctor/(?P<int:pid>)',Delete_Doctor,name="delete_doctor"),



]
