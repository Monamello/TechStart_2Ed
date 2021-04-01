from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='nome')
    description = models.CharField(max_length=30, verbose_name='descrição')
    price = models.FloatField(verbose_name='valor')
    categories = models.ManyToManyField('Category', verbose_name='categorias')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='nome')
    description = models.CharField(max_length=256, verbose_name='descrição')

    def __str__(self):
        return self.name