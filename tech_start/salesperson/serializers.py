from .models import SalesPerson
from rest_framework import serializers


class SalesPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesPerson
        fields = [ 'name', 'company_name', 'cnpj', 'email', 'telephone',
            'address', 'created_at', 'update_at'
        ]
