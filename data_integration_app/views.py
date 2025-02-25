from django.shortcuts import render

from rest_framework import viewsets

from .models import Customer, Salesman, SalesM, SalesD, ItemCard,CustCard
from .serializers import CustomerSerializer, SalesmanSerializer, SalesMSerializer, SalesDSerializer,ItemCardSerializer,CustCardSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SalesmanViewSet(viewsets.ModelViewSet):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer

class SalesMViewSet(viewsets.ModelViewSet):
    queryset = SalesM.objects.all()
    serializer_class = SalesMSerializer

class SalesDViewSet(viewsets.ModelViewSet):
    queryset = SalesD.objects.all()
    serializer_class = SalesDSerializer

class ItemCardViewSet(viewsets.ModelViewSet):
    queryset = ItemCard.objects.all()
    serializer_class = ItemCardSerializer

class CustCardViewSet(viewsets.ModelViewSet):
    queryset = CustCard.objects.all()
    serializer_class = CustCardSerializer

