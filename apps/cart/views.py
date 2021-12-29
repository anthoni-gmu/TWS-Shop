from django.shortcuts import render
from .cart import Cart
from django.conf import settings
# Create your views here.

def cart_detail(request):
    cart=Cart(request)
    productsstring =''
    
    for item in cart:
        product=item['product']
        url='/%s/%s/'%(product.category.slug,product.slug)
        b="{'id': '%s','title': '%s','price': '%s','quantity': '%s','total_price': '%s','thumbnail': '%s','url':'%s','num_available':'%s'},"%(product.id,product.title,item['price'],item['quantity'],item['total_price'],product.thumbnail.url,url,product.num_available)
        productsstring=productsstring+b
        
        
    
    context={
        'cart':cart,
        'productsstring':productsstring,
        'pub_key':settings.STRIPE_API_KEY_PUBLISHABLE,
    }
    return render(request, 'cart.html',context)