from rest_framework import serializers
from .models import Item, Book, Laptop, Phone

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'