from django.urls import path
#from django.urls import re_path as url
from resources import views


app_name='resources'

urlpatterns = [
    #path('resources/<slug:slug>/', views.resource_view, name='services'),
    path('<slug:slug>/', views.resource_view, name='resources_view'),
    ]
