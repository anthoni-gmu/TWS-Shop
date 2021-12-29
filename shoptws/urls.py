from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views

#views
from apps.store.views import product_detail,category_detail,search
from apps.core.views import frontpage
from apps.cart.views import cart_detail,success
from apps.accounts.views import signup,myaccount
from apps.order.views import admin_order_pdf

#stripe
from apps.cart.webhook import webhook

#api
from apps.store.api import api_add_to_cart,api_remove_from_cart,api_checkout, create_checkout_session
from apps.coupon.api import api_can_use

urlpatterns = [
    
    path('',frontpage,name='frontpage'),
    path('search/',search,name='search'),
    path('cart/',cart_detail,name='cart'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/',success,name='success'),
    
    path('admin/', admin.site.urls),
    path('admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    
    #Auth
    path('myaccount/',myaccount,name='myaccount'),
    path('signup/',signup,name='signup'),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    
    
    #
    
    
    #API
    path('api/can_use/',api_can_use,name='api_can_use'),
    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),
    path('api/create_checkout_session/',create_checkout_session,name='create_checkout_session'),
    path('api/checkout/',api_checkout,name='api_checkout'),
    
    path('api/remove_from_cart/',api_remove_from_cart,name='api_remove_from_cart'),
    
    #STORE
    path('<slug:category_slug>/<slug:slug>/',product_detail,name='product_detail'),
    path('<slug:category_slug>/<slug:slug>/',search,name='search'),
    path('<slug:slug>/',category_detail,name='category_detail'),
    
    
  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
