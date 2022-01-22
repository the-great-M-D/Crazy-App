from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# MAKE DYNAMIC URLS 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', views.logoutUser, name='logoutPage'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    
    
]
