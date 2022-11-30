from django.urls import path
#from django.urls import re_path as url
from papermasters import views


app_name='papermasters'

urlpatterns = [
    path('', views.home, name='home'),
    ]
