from django.urls import path
from .views import create_customer, get_all_customers, get_customer_detail, update_customer, delete_customer, login_user

urlpatterns = [
    path('customers/', create_customer, name='create_customer'),
    path('customers/all/', get_all_customers, name='get_all_customers'),
    path('customers/<str:customerId>/', get_customer_detail, name='get_customer_detail'),
    path('customers/<str:customerId>/update/', update_customer, name='update_customer'),
    path('customers/<str:customerId>/delete/', delete_customer, name='delete_customer'),
    path('users/login/', login_user, name='login_user'),  # Đổi endpoint
]