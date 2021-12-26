from django.contrib import admin
from .models import BlogPost, CategoryPost

class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title','image', 'content', 'author','category', 'created_on',)

admin.site.register(BlogPost, BlogPostAdmin)

class CategoryPostAdmin(admin.ModelAdmin):
    fields = ('title',)

admin.site.register(CategoryPost, CategoryPostAdmin)