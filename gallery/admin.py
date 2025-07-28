from django.contrib import admin
from .models import Gallery, Partners
from django.utils.html import format_html


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
    search_fields = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.image.url)
        return "No Image"

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
    search_fields = ('title',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.image.url)
        return "No Image"