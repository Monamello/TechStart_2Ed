from django.contrib import admin

from .models import Marketplace

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Marketplace)