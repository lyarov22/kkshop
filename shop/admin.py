from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['denotation', 'name', 'slug', 'weight', 'price', 'discount', 'available', 'created', 'updated']
    list_filter = ['visible', 'created', 'updated']
    list_editable = ['price', 'discount', 'available', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['img_preview']
admin.site.register(Product, ProductAdmin)