from django.urls import path
from . import views

# MAKE DYNAMIC URLS 

urlpatterns = [
    path('', views.addProduct, name='addProduct'),
    path('productupdate/', views.updateProduct, name='productUpdate')    
]
