from django.urls import path
from .views import create_cart_view, get_cart_view

urlpatterns = [
    path('create/', create_cart_view, name='create_cart'),
    path('<str:user_id>/', get_cart_view, name='get_cart'),
]
