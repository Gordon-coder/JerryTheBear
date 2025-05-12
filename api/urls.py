from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('merchandises', views.GetMerchandiseViews, 'merchandise')
router.register('Order', views.GetOrderViews, 'Order')

urlpatterns = [
    path('', include(router.urls)),  # List all merchandise items   
]
