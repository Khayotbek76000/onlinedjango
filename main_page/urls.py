from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('product/<int:pk>/', views.product_info, name='product_about'),
    path('cart/', views.cart, name='cart'),
]