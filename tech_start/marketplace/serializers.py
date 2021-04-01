from .models import Marketplace
from rest_framework import serializers


class MarketplaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marketplace
        fields = ['name', 'description', 'site', 'telephone',
            'email', 'support_contact']
