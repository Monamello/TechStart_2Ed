from .models import SalesPerson, Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'number', 'neighborhood', 'complement_address']

class SalesPersonSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = SalesPerson
        fields = [ 'name', 'company_name', 'cnpj', 'email', 'telephone',
            'address', 'created_at', 'update_at'
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        salesperson = SalesPerson.objects.create(address=address, **validated_data)
        return salesperson

    def update(self, instance, validated_data):
        address = validated_data.pop('address')
        address = instance.address
        instance.name = validated_data.get('name', instance.name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.email = validated_data.get('email', instance.email)
        instance.telephone = validated_data.get('telephone', instance.telephone)

        instance.save()
        return instance

