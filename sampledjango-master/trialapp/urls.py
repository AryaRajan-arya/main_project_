"""trialapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from data.views import *
urlpatterns =[
    path('admin/', admin.site.urls),
    path('',ListContact.as_view(), name='index'),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('add/',AddContact.as_view(), name='add'),
    path('edit/<id>/',EditContact.as_view(), name='edit'),
    path('delete/<id>/',DeleteContact.as_view(), name='delete'),
    path('submit/',List.as_view(), name='submit'),
    path('loc/',SubmitLocation.as_view(),name='loc'),
    path('var/',Var.as_view(),name='var')
    
]

