from django.contrib import admin
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display=['title', 'timestamp', 'updated']
    list_display_links=['title', 'timestamp']
    list_filter=["timestamp", "title"]
    search_fields=["title", "text", "timestamp", "updated"]
    class Meta:
      model=Posts
                   




admin.site.register(Posts, PostsAdmin)
