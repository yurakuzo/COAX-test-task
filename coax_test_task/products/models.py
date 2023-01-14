from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} | {self.category} | ₴{self.price}"


class Order(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return f"{self.username} | {self.product.name}"


class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'product_name', 'product_category', 'product_price')

    def product_name(self, obj):
        return f"{obj.product.name}"

    def product_category(self, obj):
        return f"{obj.product.category}"

    def product_price(self, obj):
        return f"{obj.product.price}"


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category', 'price']