from django.contrib import admin
from .models import Category, Product, Manufacturer, OrderItem, Order


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('model', 'manufacturer', 'price', 'availability', 'slug')

    # @admin.display(description='Price', ordering='price')
    # def get_author_name(self, obj):
    #     return obj.price


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
