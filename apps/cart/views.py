from django.shortcuts import render
from .cart import Cart
from django.conf import settings
# Create your views here.

def cart_detail(request):
    
    return render(request, 'cart.html')

def success(request):
    cart=Cart(request)
    
    cart.clear()
    return render(request, 'success.html')