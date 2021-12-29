from .cart import Cart

def cart(request):
    return{'Cartnav':Cart(request)}