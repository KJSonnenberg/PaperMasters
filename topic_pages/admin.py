from django.contrib import admin
from .models import Post, Category
from mptt.admin import DraggableMPTTAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'new_url', 'get_tags')#'meta_description',
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('category', 'title')
    search_fields = ('title', 'meta_description')
    
    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())

admin.site.register(Post, PostAdmin) 
admin.site.register(Category , DraggableMPTTAdmin)