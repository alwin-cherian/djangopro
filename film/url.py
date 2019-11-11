from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect
app_name='film'

urlpatterns = [
    path('',views.home,name='homie'),
    path('login/',views.logi,name='loginn'),
    path('logout/',views.logo,name='logouts'),
    path('register/',views.reg,name='register')
    ]
