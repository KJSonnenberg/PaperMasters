from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()
from django.urls import path, include
from django.urls import re_path as url
from django.contrib.sitemaps.views import sitemap
from topic_pages.sitemaps import *
#from . import views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

sitemaps={ 
    'static': StaticViewSitemap,
    'resourcemap': ResourceSitemap,
    #'servicemap': ServiceSitemap, 
    'subjectmap': SubtopicSitemap,
    'pagemap': PageSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),    
    path('resources/', include('resources.urls')),
    #path('services/', include('servicepages.urls')),
    path('', include('papermasters.urls')),
    path('', include('toplevel.urls')),
    path('', include('topic_pages.urls')),
    
]