from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import CartSerializer, CartItemSerializer
from datetime import datetime
from bson.objectid import ObjectId

# Tạo Cart
@api_view(['POST'])
def create_cart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        cart_data = serializer.validated_data
        cart_data['createdAt'] = datetime.now()
        cart_data['updatedAt'] = datetime.now()
        cart_collection = settings.MONGO_DB['carts']
        result = cart_collection.insert_one(cart_data)
        cart_data['_id'] = str(result.inserted_id)
        return Response(cart_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Thêm sản phẩm vào giỏ hàng
@api_view(['POST'])
def add_item_to_cart(request, cartId):
    cart_collection = settings.MONGO_DB['carts']
    cart = cart_collection.find_one({'cartId': cartId})
    if not cart:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    item_data = request.data
    item_serializer = CartItemSerializer(data=item_data)
    if not item_serializer.is_valid():
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    cart['items'].append(item_serializer.validated_data)
    cart['totalPrice'] = sum(item['price'] * item['quantity'] for item in cart['items'])
    cart['totalQuantity'] = sum(item['quantity'] for item in cart['items'])
    cart['updatedAt'] = datetime.now()

    cart_collection.update_one({'cartId': cartId}, {'$set': cart})
    cart['_id'] = str(cart['_id'])
    return Response(cart, status=status.HTTP_200_OK)

# Xóa sản phẩm khỏi giỏ hàng
@api_view(['DELETE'])
def remove_item_from_cart(request, cartId, itemId):
    cart_collection = settings.MONGO_DB['carts']
    cart = cart_collection.find_one({'cartId': cartId})
    if not cart:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    initial_len = len(cart['items'])
    cart['items'] = [item for item in cart['items'] if item['itemId'] != itemId]
    if len(cart['items']) == initial_len:
        return Response({"error": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)

    cart['totalPrice'] = sum(item['price'] * item['quantity'] for item in cart['items'])
    cart['totalQuantity'] = sum(item['quantity'] for item in cart['items'])
    cart['updatedAt'] = datetime.now()

    cart_collection.update_one({'cartId': cartId}, {'$set': cart})
    cart['_id'] = str(cart['_id'])
    return Response(cart, status=status.HTTP_200_OK)

# Cập nhật số lượng sản phẩm trong giỏ hàng
@api_view(['PUT'])
def update_item_quantity(request, cartId, itemId):
    cart_collection = settings.MONGO_DB['carts']
    cart = cart_collection.find_one({'cartId': cartId})
    if not cart:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    for item in cart['items']:
        if item['itemId'] == itemId:
            quantity = request.data.get('quantity')
            if quantity is None or not isinstance(quantity, int) or quantity < 0:
                return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)
            item['quantity'] = quantity
            break
    else:
        return Response({"error": "Item not found in cart"}, status=status.HTTP_404_NOT_FOUND)

    cart['totalPrice'] = sum(item['price'] * item['quantity'] for item in cart['items'])
    cart['totalQuantity'] = sum(item['quantity'] for item in cart['items'])
    cart['updatedAt'] = datetime.now()

    cart_collection.update_one({'cartId': cartId}, {'$set': cart})
    cart['_id'] = str(cart['_id'])
    return Response(cart, status=status.HTTP_200_OK)

# Lấy tất cả sản phẩm trong giỏ hàng
@api_view(['GET'])
def get_all_items_in_cart(request, cartId):
    cart_collection = settings.MONGO_DB['carts']
    cart = cart_collection.find_one({'cartId': cartId})
    if not cart:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    # Chuyển ObjectId thành string
    cart['_id'] = str(cart['_id'])
    return Response(cart['items'], status=status.HTTP_200_OK)