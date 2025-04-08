from django.urls import path
from .views import create_shipment, get_all_shipments, get_shipment_detail, update_shipment, delete_shipment

urlpatterns = [
    path('shipments/', create_shipment, name='create_shipment'),
    path('shipments/all/', get_all_shipments, name='get_all_shipments'),
    path('shipments/<str:shipmentId>/', get_shipment_detail, name='get_shipment_detail'),
    path('shipments/<str:shipmentId>/update/', update_shipment, name='update_shipment'),
    path('shipments/<str:shipmentId>/delete/', delete_shipment, name='delete_shipment'),
]