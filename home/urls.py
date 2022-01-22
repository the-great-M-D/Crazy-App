from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.HomePage.as_view(), name="aboutPage"),
    path('', views.DashBoard.as_view(), name="home"),
]
