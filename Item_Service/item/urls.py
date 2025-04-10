from django.urls import path
from .views import (
    create_book, get_all_books, get_book_detail, update_book, delete_book,
    create_laptop, get_all_laptops, get_laptop_detail, update_laptop, delete_laptop,
    create_phone, get_all_phones, get_phone_detail, update_phone, delete_phone,
    get_all_items  # Thêm API mới
)

urlpatterns = [
    # URL cho Book
    path('books/', create_book, name='create_book'),
    path('books/all/', get_all_books, name='get_all_books'),
    path('books/<str:itemId>/', get_book_detail, name='get_book_detail'),
    path('books/<str:itemId>/update/', update_book, name='update_book'),
    path('books/<str:itemId>/delete/', delete_book, name='delete_book'),
    # URL cho Laptop
    path('laptops/', create_laptop, name='create_laptop'),
    path('laptops/all/', get_all_laptops, name='get_all_laptops'),
    path('laptops/<str:itemId>/', get_laptop_detail, name='get_laptop_detail'),
    path('laptops/<str:itemId>/update/', update_laptop, name='update_laptop'),
    path('laptops/<str:itemId>/delete/', delete_laptop, name='delete_laptop'),
    # URL cho Phone
    path('phones/', create_phone, name='create_phone'),
    path('phones/all/', get_all_phones, name='get_all_phones'),
    path('phones/<str:itemId>/', get_phone_detail, name='get_phone_detail'),
    path('phones/<str:itemId>/update/', update_phone, name='update_phone'),
    path('phones/<str:itemId>/delete/', delete_phone, name='delete_phone'),
    # URL cho Get All Items
    path('items/all/', get_all_items, name='get_all_items'),
    
]