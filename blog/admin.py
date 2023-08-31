from django.contrib import admin

from .models import Blog

from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ['title', 'description']
    list_per_page = 10
    ordering = ('-date',)
    date_hierarchy = 'date'
    fields = ('title', 'description', 'date', 'image')


admin.site.register(Blog, BlogAdmin)

