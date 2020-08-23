from django.conf.urls import url
from django.urls import path
from . import views

from .views import *



urlpatterns=[

    #url(r'^$',index, name='index'),
    path('', views.index,name='index'),
    #url(r'^$res',index, name='index'),

    path('resources/', views.resources,name='resources'),

]
