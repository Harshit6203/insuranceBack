from django.contrib import admin
from .models import BlogPost ,Poster
from django.utils.html import format_html

from django.contrib import admin
from .models import Poster, BlogPost
from django.utils.html import mark_safe
from .models import Poster

@admin.register(Poster)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_preview']  # Add custom method to list_display

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
    image_preview.short_description = 'Image Preview'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'caption')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px; max-height:100px;" />', obj.image.url)
        else:
            return 'No Image'
    display_image.short_description = 'Image Preview'