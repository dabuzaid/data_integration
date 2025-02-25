from rest_framework import serializers
from .models import Customer, Salesman, SalesM, SalesD, ItemCard, CustCard


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = '__all__'


class SalesMSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesM
        fields = '__all__'


class SalesDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesD
        fields = '__all__'


class ItemCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCard
        fields = '__all__'


class CustCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustCard
        fields = '__all__'
