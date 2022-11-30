from django.urls import path
from django.urls import re_path as url
from topic_pages import views


app_name='topic_pages'

urlpatterns = [ 
    url(r'^(?P<hierarchy>.+)/$', views.show_category, name='category'),
    path('search', views.search_view, name='search_view')
   ]