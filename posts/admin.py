from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
   
    list_display=['title', 'timestamp', 'updated']
    list_filter=["title", "timestamp"
                 ]
    list_display_links=['title', 'timestamp']
    search_fields=["title", "content"]
    




admin.site.register(Post, PostAdmin)
