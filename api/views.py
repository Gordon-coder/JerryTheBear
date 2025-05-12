from django.shortcuts import render
from django.http import HttpResponse
from .models import Merchandise, Order
from .serializers import MerchandiseSerializer, OrderSerializer
from rest_framework import viewsets

# Create your views here.
class GetMerchandiseViews(viewsets.ModelViewSet):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()
    
class GetOrderViews(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()