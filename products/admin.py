from django.contrib import admin
from .models import Product, Category
# from .models import Product, Category, ProductReview

# Selects which details will be shown in the Django admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
      'p_id',
      'name',
      'category',
      'price',
      'rating',
      'image',
    )

    # Items are ordered in admin by category first then alphabetically by name
    ordering = ('category', 'name')


# Selects which details will be shown in the Django admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
      'friendly_name',
      'name',
    )


# class ProductReviewAdmin(admin.ModelAdmin):
#     list_display = (
#       'review_title',
#       'reviewed_product',
#       'reviewer',
#       'date',
#     )

#     ordering = ('reviewer', 'date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductReview, ProductReviewAdmin)