from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
      'p_id',
      'name',
      'category',
      'price',
      'rating',
      'image',
    )

    # Items are ordered by category 1st then alphabetically by name
    ordering = ('category', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
      'friendly_name',
      'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)