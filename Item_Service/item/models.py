from django.db import models

class Item(models.Model):
    itemId = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stockQuantity = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = False  # Không phải abstract để có thể tạo bảng riêng

class Book(Item):
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publicationYear = models.IntegerField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} by {self.author}"

class Laptop(Item):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.IntegerField()
    screenSize = models.FloatField()

    def __str__(self):
        return f"{self.brand} {self.model}"

class Phone(Item):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    operatingSystem = models.CharField(max_length=50)
    ram = models.IntegerField()
    storage = models.IntegerField()
    cameraResolution = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model}"

from django.apps import AppConfig

class ItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item'