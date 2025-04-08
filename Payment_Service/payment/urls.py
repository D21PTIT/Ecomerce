from django.urls import path
from .views import create_payment, get_all_payments, get_payment_detail, update_payment, delete_payment

urlpatterns = [
    path('payments/', create_payment, name='create_payment'),
    path('payments/all/', get_all_payments, name='get_all_payments'),
    path('payments/<str:paymentId>/', get_payment_detail, name='get_payment_detail'),
    path('payments/<str:paymentId>/update/', update_payment, name='update_payment'),
    path('payments/<str:paymentId>/delete/', delete_payment, name='delete_payment'),
]