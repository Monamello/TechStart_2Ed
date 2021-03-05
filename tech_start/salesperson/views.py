from django.shortcuts import render
from .models import SalesPerson
from rest_framework import viewsets
from .serializers import SalesPersonSerializer

class SalesPersonViewSet(viewsets.ModelViewSet):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer
