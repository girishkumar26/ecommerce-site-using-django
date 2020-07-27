from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product-single', views.product, name='product-single'),
    path('cart.html', views.cart, name='cart'),
    path('shop.html', views.shop, name='shop'),
    path('checkout.html', views.checkout, name='checkout'),

]
