from django.db import models

class Shipment(models.Model):
    shipmentId = models.CharField(max_length=50, primary_key=True)
    orderId = models.CharField(max_length=50)
    customerAddress = models.CharField(max_length=255)
    shipmentStatus = models.CharField(max_length=50)
    shipmentDate = models.DateField(auto_now_add=True)
    estimatedDeliveryDate = models.DateField()
    carrier = models.CharField(max_length=100)
    trackingNumber = models.CharField(max_length=100)

    def __str__(self):
        return f"Shipment {self.shipmentId} for Order {self.orderId}"

from django.apps import AppConfig

class ShipmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shipment'