from django.urls import path
from .views import add_item_view, get_item_view, get_items_view

urlpatterns = [
    path('add/', add_item_view, name='add_item'),  # API thêm sản phẩm
    path('<str:item_id>/', get_item_view, name='get_item'),  # API lấy sản phẩm theo ID
    path('category/<str:category>/', get_items_view, name='get_items_by_category'),  # API lấy sản phẩm theo loại
]
