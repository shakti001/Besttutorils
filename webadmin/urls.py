from django.urls import path , include
from django.contrib import admin
from . import views 
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [
    path('', views.login , name='login'),

    path('index/', views.index , name='index' ),
    path('contact/', views.contact, name='contact'),
    path('del_contact/<int:id>', views.del_contact, name='del_contact'),

    path('main/', views.main , name='main' ),

    path('course/', views.course , name='course' ),
    path('add_course/', views.add_course , name='add_course' ),
    path('edit_course/<id>', views.edit_course , name='edit_course' ),

    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('topic/', views.topic , name='topic' ),
    path('add_topic/', views.add_topic , name='add_topic' ),
    path('edit_topic/', views.edit_topic , name='edit_topic' ),
    path('del_topic/<int:id>', views.del_topic , name='del_topic' ),

    path('edit_topic/<id>', views.edit_topic , name='edit_topic' ),
    path('user/', views.user , name='user' ),
    path('del_user/<int:id>', views.del_user , name='del_user' ),

    path('slider/', views.slider , name='slider' ),
    path('create_slider/', views.create_slider , name='create_slider' ),
    path('edit_slider/<id>', views.edit_slider , name='edit_slider' ),
    path('del_slider/<id>', views.del_slider , name='del_slider' ),





]