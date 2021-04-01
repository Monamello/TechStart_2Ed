from django.contrib import admin
from .models import Product, Category
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Category)