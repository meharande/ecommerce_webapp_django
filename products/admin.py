from django.contrib import admin

from .models import (
    Categories,
    Option,
    OptionItem,
    OptionGroup,
    ProductVariant,
    Product,
    ProductVariantValues,
    Brand
)
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']

class OptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class OptionGroupAdmin(admin.ModelAdmin):
    pass

class OptionItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'option_group', 'name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_id', 'name', 'created_at', 'status']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']




admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Option, OptionsAdmin)
admin.site.register(OptionGroup, OptionGroupAdmin)
admin.site.register(OptionItem, OptionItemAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

