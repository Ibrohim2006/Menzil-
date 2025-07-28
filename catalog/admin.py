from django.contrib import admin
from .models import Category, Product, Material
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('category', 'name', 'description', 'image_tag')
    search_fields = ('name', 'description')
    list_filter = ('category',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return ""

@admin.register(Material)
class MaterialAdmin(TranslatableAdmin):  
    list_display = ('category', 'name', 'description', 'image_tag')
    search_fields = ('name', 'description')
    list_filter = ('category',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return ""