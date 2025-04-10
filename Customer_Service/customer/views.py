from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
import requests

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        # Lưu khách hàng vào cơ sở dữ liệu
        customer = serializer.save()
        
        # Tạo giỏ hàng cho khách hàng
        cart_data = {
            "cartId": f"CART-{customer.id}",  # Sử dụng CART-<customerId>
            "customerId": customer.id,
            "items": [],
            "totalPrice": 0,
            "totalQuantity": 0,
            "notes": ""
        }
        
        try:
            # Gọi API của Cart_Service để tạo giỏ hàng
            response = requests.post('http://127.0.0.1:8002/api/carts/', json=cart_data)
            if response.status_code != status.HTTP_201_CREATED:
                customer.delete()
                return Response({"error": "Failed to create cart for customer", "details": response.json()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.exceptions.RequestException as e:
            customer.delete()
            return Response({"error": f"Failed to create cart: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customer_detail(request, customerId):
    try:
        customer = Customer.objects.get(id=customerId)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_customer(request, customerId):
    try:
        customer = Customer.objects.get(id=customerId)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_customer(request, customerId):
    try:
        customer = Customer.objects.get(id=customerId)
        customer.delete()
        return Response({"message": "Customer deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = Customer.objects.get(email=email)
        if password == customer.password:
            serializer = CustomerSerializer(customer)
            customer_data = serializer.data
            customer_data.pop('password', None)
            return Response({
                "message": "Login successful",
                "customer": customer_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
    except Customer.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)