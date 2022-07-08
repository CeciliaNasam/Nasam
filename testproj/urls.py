"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from testapp import views
from django.urls import re_path as url

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('registedperson/', views.registedperson, name = 'registedperson'),
    path('personal_info_form/', views.personal_info, name = 'personal_info_form'),
    url(r'^index2/(\d+)/$', views.index2, name = 'index2'),
    url(r'^index3/(\d+)/(\d+)/$', views.index3, name = 'index3'),
    url(r'^delete/(\d+)/$', views.delete, name = 'delete'),
    path('vaccine_list1/', views.second, name = 'vaccine_list1'),
    path('vaccine_list2/', views.second2, name = 'vaccine_list2'),
    path('about_us/', views.third, name = 'about_us'),
    path('pfizer/', views.pfizer, name = 'pfizer'),
    path('moderna/', views.moderna, name = 'moderna'),
    path('sputnik/', views.sputnik, name = 'sputnik'),
    path('janssen/', views.janssen, name = 'janssen'),
    path('astra/', views.astra, name = 'astra'),
    path('covaxin/', views.covaxin, name = 'covaxin'),
    path('coronavac/', views.coronavac, name = 'coronavac'),
    path('sinopharm/', views.sinopharm, name = 'sinopharm'),
    path('reach/', views.reach, name = 'reach_us'),
    path('faq/', views.faq, name = 'frequently_asked_questions'),
    path('edit/', views.Edit, name = 'Edit'),
    ]