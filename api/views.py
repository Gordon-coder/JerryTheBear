from django.shortcuts import render
from django.http import HttpResponse
from .models import Merchandise
from .serializers import MerchandiseSerializer

# Create your views here.
def getMerchandiseViews(request):
    queryset = Merchandise.objects.all()
    serializer = MerchandiseSerializer(queryset, many=True)
    return HttpResponse(serializer.data, content_type='application/json')
