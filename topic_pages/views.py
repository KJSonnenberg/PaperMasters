from django.shortcuts import render, get_object_or_404   
from .models import Category, Post 
from taggit.models import Tag
from django.db.models import Count 
 

def show_category(request, hierarchy= None,):
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_object_or_404(Post, slug = category_slug[-1])
        tags = Tag.objects.all()  
        topic_tags_ids = instance.tags.values_list('id', flat=True)
        topics = Post.objects.filter(tags__in=topic_tags_ids)\
                                  .exclude(id=instance.id)
        topics = topics.annotate(same_tags=Count('tags'))\
                                .order_by('title')#[:4] 
        posts = Post.objects.prefetch_related('tags').filter(slug=category_slug[-1]) #this alone works
        posts = posts.filter(slug=category_slug[-1])
    
        return render(request, "topic_pages/postDetail.html", {'instance':instance,
                                                                'topics':topics,
                                                                'tags':tags,
                                                                'posts':posts})
    else:
        return render(request, 'topic_pages/categories.html', {'instance':instance})

        #{% url 'topic_pages:subjects' topics.new_url %}#something like this for linking 
        
def search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        topics = Post.objects.filter(content__contains=searched)
        return render(request, 
        'topic_pages/search.html',
        {'searched': searched,
         'topics': topics })
    else:                  
        return render(request, 
        'topic_pages/search.html', 
        {})