from django.contrib import admin

from .models import Category,Brand,Product,ProductImage, ProductSpecification
# # Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model=ProductImage
class ProductSpecificationAdmin(admin.StackedInline):
    model = ProductSpecification 
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin,ProductSpecificationAdmin] 

# admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
