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
TYPE_OF_RESOURCE = (
        ('E', 'Elements of a Paper'),
        ('R', 'Type of Research'),
        ('P', 'Type of Paper'),
    )
class ResourceModel(models.Model):
    id =  models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_CHOICES)
    resources_tags = TaggableManager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null = True, unique = True, blank = True)
    meta_title = models.CharField(max_length=200, blank=True)
    type_of_resource = models.CharField(max_length=1, choices=TYPE_OF_RESOURCE)  
    meta_description = models.CharField(max_length=400)
    content = RichTextField(blank=True)
    old_url = models.CharField(max_length=200,blank=True) 
    notes = models.TextField(null = True, blank=True)
    class Meta:
            verbose_name = 'Resource'
            verbose_name_plural = 'Resources'
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('resources:resources_view', kwargs={'slug': self.slug}) 
