from django.shortcuts import render
from servicepages.models import Service 
from taggit.models import Tag
from django.db.models import Count 

def services_view(request, slug):
    slug = slug
    servicing = Service.objects.get(slug=slug)
    tags = Tag.objects.all()  
    topic_tags_ids = servicing.service_tags.values_list('id', flat=True)
    service = Service.objects.filter(service_tags__in=topic_tags_ids)\
                                  .exclude(id=servicing.id)
    service = service.annotate(same_tags=Count('service_tags'))\
                                .order_by('title')#[:4] 
    posts = Service.objects.prefetch_related('tags').filter(slug=slug)
    posts = posts.filter(slug=slug) 

    return render(request, 'servicepages/services.html', {'servicing':servicing,
                                                        'service': service,
                                                        'tags':tags,
                                                        'posts':posts})  


    #{% url 'topic_pages:subject' post.new_url %} use this for later 
