from django.contrib import admin
from .models import Brand, Product, Category



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", 'slug', "brand", "description", "image", "status"]
    list_filter = ["brand", "price", "posted_by", "status"]
    search_fields = ["name", "price", "posted_by"]


admin.site.register([Brand, Category])