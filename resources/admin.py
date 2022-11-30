from django.contrib import admin
from .models import ResourceModel

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_resource', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ResourceModel, ResourceAdmin)
