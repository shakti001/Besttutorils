from django.urls import path , include
from django.contrib import admin
from . import views 
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [
    path('', views.index , name='index' ),
    path('contact/', views.contact , name='contact' ),
    path('tutorial/', views.tutorial , name='tutorial' ),
    path('general_setting/', views.general_setting , name='general_setting' ),

    path('caurse/', views.caurse , name='caurse' ),
    path('single_caurse/<int:id>', views.single_caurse , name='single_caurse' ),\
    path('topic_read/<int:id>', views.topic_read , name='topic_read' ),




    path('register/', views.register , name='register' ),
    path('login/', views.login , name='login' ),
    path('logout/', views.logout , name='logout' ),





]