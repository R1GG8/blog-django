from django.contrib import admin
from .models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'status', 'published']
    list_display_links = ['id', 'title']
    list_filter = ['author', 'category', 'status']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'author']
    search_fields = ['author']