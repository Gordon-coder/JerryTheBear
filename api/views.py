from django.shortcuts import render
from django.http import HttpResponse
from .models import Merchandise
from .serializers import MerchandiseSerializer
from rest_framework import viewsets

# Create your views here.
class GetMerchandiseViews(viewsets.ViewSet):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()
    
