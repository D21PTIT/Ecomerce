from django.urls import path
from .views import create_order, get_all_orders, get_order_detail, update_order, delete_order

urlpatterns = [
    path('orders/', create_order, name='create_order'),
    path('orders/all/', get_all_orders, name='get_all_orders'),
    path('orders/<str:orderId>/', get_order_detail, name='get_order_detail'),
    path('orders/<str:orderId>/update/', update_order, name='update_order'),
    path('orders/<str:orderId>/delete/', delete_order, name='delete_order'),
]