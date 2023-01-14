from django.contrib import admin

from .models import Category, Product, Order, ProductAdmin, OrderAdmin


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
