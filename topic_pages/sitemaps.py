from django.contrib.sitemaps import Sitemap 
from django.contrib import sitemaps
from django.shortcuts import reverse
from resources.models import ResourceModel
from servicespages.models import Service
from .models import Post, Category
import datetime


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'yearly'
    lastmod = datetime.datetime.now()

    def items(self):
        return [
            'papermasters:home',
            'toplevel:service_page', 
            'toplevel:prices',
            'toplevel:subjects_page',
            'toplevel:resources_page',
            'toplevel:order', 
            'toplevel:about_us',
            'toplevel:faq', 
            'toplevel:contact',  
            'toplevel:writing_opp',       
            'toplevel:terms_use', 
            'toplevel:guarantees', 
            'toplevel:privacy_policy',  
            'topic_pages:anthropology',  
            'topic_pages:art', 
            'topic_pages:business',  
            'topic_pages:criminal_justice', 
            'topic_pages:economics', 
            'topic_pages:education', 
            'topic_pages:geography', 
            'topic_pages:literature',
            'topic_pages:medical', 
            'topic_pages:military', 
            'topic_pages:nursing', 
            'topic_pages:philosophy', 
            'topic_pages:political_science', 
            'topic_pages:psychology', 
            'topic_pages:religion', 
            'topic_pages:science', 
            'topic_pages:sociology', 
            'topic_pages:technology', 
            'topic_pages:us_history',
            'topic_pages:world_history', 
            ]

    def location(self, item):
        return reverse(item)

class SubtopicSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https" 
    
    def items(self):
        return Category.objects.all()  

    def location(self, obj):
        return f"/{obj.new_url}" 

    def lastmod(self, obj):
        return obj.last_update

class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https" 
    
    def items(self):
        return Post.objects.all()  

    def location(self, obj):
        return f"/{obj.new_url}" 

    def lastmod(self, obj):
        return obj.last_update 

class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https" 
    
    def items(self):
        return Service.objects.all() 
    
    def lastmod(self, obj):
        return obj.last_update

class ResourceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https" 
    
    def items(self):
        return ResourceModel.objects.all()  
    
    def lastmod(self, obj):
        return obj.last_update
