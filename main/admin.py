from django.contrib.admin.decorators import register
from django.contrib import admin

from .models import Articles

@register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publication_date')
    search_fields = ['title', 'content']
