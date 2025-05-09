from rest_framework import serializers
from .models import Merchandise

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = ['id', 'name', 'price', 'image', 'stock']