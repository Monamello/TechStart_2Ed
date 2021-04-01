from .models import Product, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'name', 'description']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = [ 'name', 'description', 'price', 'categories']

