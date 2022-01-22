from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="homepage"),
    path('home', views.DashBoard.as_view(), name="home"),
]
