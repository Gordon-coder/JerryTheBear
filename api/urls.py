from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'merchandises', views.GetMerchandiseViews, 'merchandise')

urlpatterns = [
    path('', include(router.urls))  # List all merchandise items
]
