from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer

@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_payment_detail(request, paymentId):
    try:
        payment = Payment.objects.get(paymentId=paymentId)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_payment(request, paymentId):
    try:
        payment = Payment.objects.get(paymentId=paymentId)
        serializer = PaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_payment(request, paymentId):
    try:
        payment = Payment.objects.get(paymentId=paymentId)
        payment.delete()
        return Response({"message": "Payment deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)