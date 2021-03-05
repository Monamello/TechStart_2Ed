from django.contrib import admin
from .models import SalesPerson
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(SalesPerson)