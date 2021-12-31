from .cart import Cart
from django.conf import settings

def cart(request):
    
    cart=Cart(request)
    productsstring =''
    
    for item in cart:
        product=item['product']
        url='/%s/%s/'%(product.category.slug,product.slug)
        b="{'id': '%s','title': '%s','price': '%s','quantity': '%s','total_price': '%s','thumbnail': '%s','url':'%s','num_available':'%s'},"%(product.id,product.title,item['price'],item['quantity'],item['total_price'],product.thumbnail.url,url,product.num_available)
        productsstring=productsstring+b
    
    if request.user.is_authenticated:
        first_name=request.user.first_name
        last_name=request.user.last_name
        email=request.user.email
        address=request.user.userprofile.address
        zipcode=request.user.userprofile.zipcode
        place=request.user.userprofile.place
        phone=request.user.userprofile.phone
    else:
        first_name=last_name=email=address= zipcode= place= phone=''    
    
    context={
        'cart':cart,
        'productsstring':productsstring,
        'pub_key':settings.STRIPE_API_KEY_PUBLISHABLE,
        'first_name':first_name,
        'last_name':last_name,
        'email':email,
        'address':address,
        'zipcode':zipcode,
        'place':place,
        'phone':phone
    }
    
    return context
