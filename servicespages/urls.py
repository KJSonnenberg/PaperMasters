from django.urls import path
#from django.urls import re_path as url
from . import views


app_name='servicepages'

urlpatterns = [   
    #path('services/<slug:slug>/', views.services_view, name='services'),
    path('<slug:slug>/', views.services_view, name='services'), 
    ] 