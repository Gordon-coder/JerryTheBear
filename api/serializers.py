from rest_framework import serializers
from .models import Merchandise, Order

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = ['id', 'name', 'price', 'image', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'merchandise', 'name', 'quantity', 'phone_number', 'created_at', 'resolved']