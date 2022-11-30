from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField



STATUS_CHOICES = (
    ('ur', 'Urgent'),
    ('ac', 'Acceptable'),
    ('op', 'Optimized'),
)
class Service(models.Model):
    id =  models.IntegerField(primary_key=True)
    service_tags = TaggableManager()
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_CHOICES)
    title = models.CharField(max_length=200, unique=True, blank=True, null=True)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True) 
    meta_description = models.CharField(max_length=400)
    content = RichTextField()
    old_url = models.CharField(max_length=200,blank=True)
    notes = models.TextField(null = True, blank=True)


    class Meta:
            verbose_name = 'Service'
            verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.slug)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('servicepages:services', args=[str(self.slug)])
