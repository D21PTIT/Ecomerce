from rest_framework import serializers

class CartItemSerializer(serializers.Serializer):
    itemId = serializers.CharField(max_length=50)
    quantity = serializers.IntegerField()
    price = serializers.FloatField()  # Chuyển từ DecimalField thành FloatField

class CartSerializer(serializers.Serializer):
    cartId = serializers.CharField(max_length=50)
    customerId = serializers.CharField(max_length=50)
    items = CartItemSerializer(many=True)
    totalPrice = serializers.FloatField()  # Chuyển từ DecimalField thành FloatField
    totalQuantity = serializers.IntegerField()
    createdAt = serializers.DateTimeField(required=False)
    updatedAt = serializers.DateTimeField(required=False)
    notes = serializers.CharField(max_length=255, allow_blank=True)