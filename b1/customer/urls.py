from django.urls import path
from .views import register_customer, login_customer

urlpatterns = [
    path('register/', register_customer, name='register_customer'),  # API Đăng ký
    path('login/', login_customer, name='login_customer'),  # API Đăng nhập
]
