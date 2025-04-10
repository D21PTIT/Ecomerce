from django.db import models

class Customer(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    accountId = models.CharField(max_length=100)
    fullnameId = models.CharField(max_length=255)
    addressId = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Trường password đã được thêm
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullnameId

