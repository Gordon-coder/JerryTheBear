from django.contrib import admin
from .models import Merchandise, Order
# Register your models here.

class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('stock', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('merchandise', 'name', 'quantity', 'phone_number')
    search_fields = ('name', 'phone_number')
    list_filter = ('merchandise',)

admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(Order, OrderAdmin)