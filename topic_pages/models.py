from django.db import models
from django.utils.text import slugify 
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
  id = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=120)
  category = TreeForeignKey('Category',null=True,blank=True, on_delete=models.CASCADE)
  tags = TaggableManager()
  slug = models.SlugField(max_length = 150)
  meta_title = models.CharField(max_length=250, blank=True)
  meta_description = models.TextField(blank=True, null=True)
  content = RichTextField(blank=True)
  old_url = models.CharField(max_length=255, blank=True) 
  new_url = models.CharField(max_length=255)
  updated = models.DateField(blank=True, null=True)


  def __str__(self):
    return self.title
  
  class Meta: 
        verbose_name = "Topic"
        verbose_name_plural = "Topics" 

  def get_absolute_url(self):
    return reverse('topic_pages:category', args=[self.new_url])

class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField()
  meta_title = models.CharField(max_length=200, blank=True)
  meta_description = models.TextField(blank=True)
  content = models.TextField(blank=True) 
  old_url = models.CharField(max_length=255, blank=True) 
  new_url = models.CharField(max_length=255)


  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'Subtopics'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name