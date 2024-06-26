from django.contrib import admin
from .models import Product
from .models import Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock','category', 'updated_date', 'is_available')
    list_display_links=('product_name', 'category')
    prepopulated_fields={'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value','is_active')
    list_editable=('is_active',)
    list_filter =('product', 'variation_category', 'variation_value')
admin.site.register(Variation, VariationAdmin)