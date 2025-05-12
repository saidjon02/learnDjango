from django.contrib import admin
from .models import Post, Tag, Profile, PostTag

# Postni admin panelida ko'rsatish
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'content')

# Tagni admin panelida ko'rsatish
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile)
admin.site.register(PostTag)
