from django.urls import path
from .views import *

urlpatterns = [
    path('', getMerchandiseViews)  # List all merchandise items
]
