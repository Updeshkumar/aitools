from django.contrib import admin
from .models import blog

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'slug', 'image']
    list_filter = ['title',]
    prepopulated_fields = {'slug': ('title', )}