from marketplace.models import Marketplace
from rest_framework import viewsets
from .serializers import MarketplaceSerializer


class MarketplaceViewSet(viewsets.ModelViewSet):
    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer
