from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductsList.as_view(), name='product_all'),
]