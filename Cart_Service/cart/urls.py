from django.urls import path
from .views import create_cart, add_item_to_cart, remove_item_from_cart, update_item_quantity, get_all_items_in_cart

urlpatterns = [
    path('carts/', create_cart, name='create_cart'),
    path('carts/<str:cartId>/add-item/', add_item_to_cart, name='add_item_to_cart'),
    path('carts/<str:cartId>/remove-item/<str:itemId>/', remove_item_from_cart, name='remove_item_from_cart'),
    path('carts/<str:cartId>/update-quantity/<str:itemId>/', update_item_quantity, name='update_item_quantity'),
    path('carts/<str:cartId>/items/', get_all_items_in_cart, name='get_all_items_in_cart'),
]