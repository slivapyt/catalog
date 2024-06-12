from django.contrib import admin
from catalog.models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'description',)
    list_filter = ('category',)
    search_fields = ('category', 'description',)


@admin.register(Product)
class ProductgAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'description',)
    list_filter = ('category',)
    search_fields = ('category', 'description',)
