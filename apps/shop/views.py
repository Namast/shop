from django.shortcuts import render
from django.views.generic import ListView

from apps.shop.models import Product


class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = 'shop/product-list.html'
