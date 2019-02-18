'''
Created on Jan. 26, 2019

@author: Louis-Philippe
'''
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]