from django.contrib import admin
from django.db.models import fields
from django.utils.safestring import mark_safe
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'get_html_photo', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('time_create',)
    prepopulated_fields = {'slug':('title',)}
    fields = ('title', 'content', 'photo', 'slug', 'cat', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel for admin users'