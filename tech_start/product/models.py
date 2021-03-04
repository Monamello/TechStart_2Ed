from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='nome')
    description = models.CharField(max_length=30, verbose_name='descrição')
    price = models.IntegerField(verbose_name='valor')
    categories = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='categorias', null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='nome')
    description = models.CharField(max_length=256, verbose_name='descrição')

    def __str__(self):
        return self.name