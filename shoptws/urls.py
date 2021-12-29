from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.store.views import product_detail,category_detail,search
from apps.core.views import frontpage
from apps.cart.views import cart_detail


from apps.store.api import api_add_to_cart,api_remove_from_cart

from apps.coupon.api import api_can_use

urlpatterns = [
    
    path('',frontpage,name='frontpage'),
    path('search/',search,name='search'),
    path('cart/',cart_detail,name='cart'),
    
    path('admin/', admin.site.urls),
    
    #API
    path('api/can_use/',api_can_use,name='api_can_use'),
    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),
    path('api/remove_from_cart/',api_remove_from_cart,name='api_remove_from_cart'),
    
    #STORE
    path('<slug:category_slug>/<slug:slug>/',product_detail,name='product_detail'),
    path('<slug:category_slug>/<slug:slug>/',search,name='search'),
    path('<slug:slug>/',category_detail,name='category_detail'),
    
    
  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
