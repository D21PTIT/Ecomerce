from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ORDER_COLLECTION, OrderSerializer
from datetime import datetime

@api_view(['POST'])
def create_order(request):
    # Thêm orderDate nếu không có trong request
    data = request.data.copy()
    if 'orderDate' not in data:
        data['orderDate'] = datetime.now().isoformat()

    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        # Kiểm tra xem orderId đã tồn tại chưa
        if ORDER_COLLECTION.find_one({"orderId": data.get("orderId")}):
            return Response({"error": "Order with this orderId already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Chèn dữ liệu vào MongoDB
        serializer.create(serializer.validated_data)
        # Lấy lại bản ghi từ MongoDB để bao gồm _id
        created_order = ORDER_COLLECTION.find_one({"orderId": data.get("orderId")})
        # Chuyển _id thành chuỗi
        created_order['_id'] = str(created_order['_id'])
        return Response(created_order, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_orders(request):
    orders = list(ORDER_COLLECTION.find())
    # Chuyển ObjectId thành string để trả về JSON
    for order in orders:
        order['_id'] = str(order['_id'])
    return Response(orders, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_detail(request, orderId):
    order = ORDER_COLLECTION.find_one({"orderId": orderId})
    if order:
        order['_id'] = str(order['_id'])
        return Response(order, status=status.HTTP_200_OK)
    return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_order(request, orderId):
    order = ORDER_COLLECTION.find_one({"orderId": orderId})
    if not order:
        return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        updated_order = serializer.update(order, serializer.validated_data)
        updated_order['_id'] = str(updated_order['_id'])
        return Response(updated_order, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_order(request, orderId):
    result = ORDER_COLLECTION.delete_one({"orderId": orderId})
    if result.deleted_count > 0:
        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)