from django.shortcuts import render
from .models import Product, Category
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import FilterSet
from rest_framework import filters, generics

class DynamicSearchFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'contains'],
            'description': ['exact', 'contains'],
            'price': ['exact', 'lt', 'gt'],
            'categories': ['exact'],
        }
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = DynamicSearchFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
