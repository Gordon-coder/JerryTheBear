from django.contrib import admin
from .models import Merchandise
# Register your models here.

class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('stock', 'price')

admin.site.register(Merchandise, MerchandiseAdmin)