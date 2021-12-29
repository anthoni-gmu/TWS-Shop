from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Category
from django.db.models import Q

import random

def search(request):
    query=request.GET.get('query')
    instock=request.GET.get('instock')
    price_from=request.GET.get('price_from',0)
    price_to=request.GET.get('price_to',100000)
    sorting=request.GET.get('sorting','-date_added')
    products=Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)
    if instock:
        products=products.filter(num_available__gte=1)
    context={
        'query':query,
        'products':products.order_by(sorting),
        'price_from':price_from,
        'instock':instock,
        'price_to':price_to,
        'sorting':sorting
    }
    
    return render(request,'search.html',context)


def product_detail(request,category_slug,slug):
    product=get_object_or_404(Product,slug=slug)
    context={
        'product':product,
    }
    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    print("hola")
    category=get_object_or_404(Category,slug=slug)
    
    
    products=category.products.filter(parent=None)
    context={
        'category':category,
        'products':products,
    }
    return render(request, 'category_detail.html', context)

