from django.db import models

class Payment(models.Model):
    paymentId = models.CharField(max_length=50, primary_key=True)
    orderId = models.CharField(max_length=50)
    amount = models.FloatField()
    paymentMethod = models.CharField(max_length=50)
    paymentStatus = models.CharField(max_length=50)
    paymentDate = models.DateField(auto_now_add=True)
    transactionId = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.paymentId} for Order {self.orderId}"

from django.apps import AppConfig

class PaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment'