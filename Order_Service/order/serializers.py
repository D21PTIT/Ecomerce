from rest_framework import serializers
from django.conf import settings

# Định nghĩa collection
ORDER_COLLECTION = settings.MONGO_DB["order"]  # Tên collection

# Serializer để kiểm tra và chuyển đổi dữ liệu
class OrderSerializer(serializers.Serializer):
    orderId = serializers.CharField(max_length=50)
    customerId = serializers.CharField(max_length=50)
    items = serializers.ListField(child=serializers.DictField())  # Danh sách các item
    totalAmount = serializers.FloatField()
    orderStatus = serializers.CharField(max_length=50)
    orderDate = serializers.DateTimeField(required=False)
    paymentId = serializers.CharField(max_length=50)
    shipmentId = serializers.CharField(max_length=50)

    def create(self, validated_data):
        # Thêm dữ liệu vào MongoDB
        return ORDER_COLLECTION.insert_one(validated_data)

    def update(self, instance, validated_data):
        # Cập nhật dữ liệu trong MongoDB
        ORDER_COLLECTION.update_one(
            {"orderId": instance["orderId"]},
            {"$set": validated_data}
        )
        return ORDER_COLLECTION.find_one({"orderId": instance["orderId"]})