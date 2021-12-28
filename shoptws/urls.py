from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.store.views import product_detail,category_detail
from apps.core.views import frontpage

urlpatterns = [
    path('',frontpage,name='frontpage'),
    path('admin/', admin.site.urls),
    
    path('<slug:category_slug>/<slug:slug>/',product_detail,name='product_detail'),
    path('<slug:slug>/',category_detail,name='category_detail'),
  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
