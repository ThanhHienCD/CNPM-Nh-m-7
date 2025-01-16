from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('pas/', views.pas, name="pas"),
    path('checkout/', views.checkout, name="checkout"),
]
