from django.shortcuts import render, get_object_or_404 
from resources.models import ResourceModel
from taggit.models import Tag
from django.db.models import Count 

def resource_view(request, slug):
    slug = slug
    resourcing = ResourceModel.objects.get(slug=slug)
    tags = Tag.objects.all()  
    topic_tags_ids = resourcing.resources_tags.values_list('id', flat=True)
    resources = ResourceModel.objects.filter(resources_tags__in=topic_tags_ids)\
                                  .exclude(id=resourcing.id)
    resources = resources.annotate(same_tags=Count('resources_tags'))\
                                .order_by('title')#[:4] 
    posts = ResourceModel.objects.prefetch_related('tags').filter(slug=slug)
    posts = posts.filter(slug=slug) 

    return render(request, 'resources/resources.html', {'resourcing':resourcing,
                                                        'resources': resources,
                                                        'tags':tags,
                                                        'posts':posts})  


    #{% url 'topic_pages:subject' post.new_url %} use this for later 
