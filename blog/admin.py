from django.contrib import admin
from blog.models import Material
# Register your models here.


@admin.register(Material)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    search_fields = ('title', 'body',)
