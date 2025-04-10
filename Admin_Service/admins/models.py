from django.db import models

class Admin(models.Model):
    adminId = models.CharField(max_length=50, primary_key=True)
    adminName = models.CharField(max_length=100)
    adminRole = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"Admin {self.adminId} - {self.adminName}"