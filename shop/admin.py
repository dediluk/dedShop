from django.contrib import admin
from .models import Category, Product, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('model', 'manufacturer', 'price', 'availability', 'slug')

    # @admin.display(description='Price', ordering='price')
    # def get_author_name(self, obj):
    #     return obj.price


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer)
