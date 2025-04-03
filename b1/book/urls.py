from django.urls import path
from .views import add_book_view, get_book_view, get_all_books_view, update_book_view, delete_book_view

urlpatterns = [
    path('add/', add_book_view, name='add_book'),  # API thêm sách
    path('<str:book_id>/', get_book_view, name='get_book'),  # API lấy sách theo ID
    #path('all/', get_all_books_view, name='get_all_books'),  # API lấy danh sách tất cả sách
    #path('update/<str:book_id>/', update_book_view, name='update_book'),  # API cập nhật sách
    #path('delete/<str:book_id>/', delete_book_view, name='delete_book'),  # API xóa sách
]
