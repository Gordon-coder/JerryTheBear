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

def order_item(request):
    if request.method == 'POST':
        return HttpResponse("Invalid request method.", status=405)
    
    merchandise_id = request.GET.get('merch_id')
    name = request.GET.get('name')
    quantity = request.GET.get('amount')
    phone_number = request.GET.get('phone')

    # Validate the input data
    if not name:
        return HttpResponse("Name is required.", status=400)
    if not quantity:
        return HttpResponse("Quantity is required.", status=400)
    if not phone_number:
        return HttpResponse("Phone number is required.", status=400)

    # Create a new order
    order = Order(merchandise_id=merchandise_id, name=name, quantity=quantity, phone_number=phone_number)
    order.save()

    return HttpResponse("Order placed successfully, you will be contacted shortly on Whatsapp for payment.", status=200)