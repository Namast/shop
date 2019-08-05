from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductsList.as_view(), name='product_all'),
    path('detail/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path("add-cartitem/<slug:slug>/<int:pk>/", AddCartItem.as_view(), name="add_cartitem"),
    path("cart/", CartItemList.as_view(), name="cart_item"),
]