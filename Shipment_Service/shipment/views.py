from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer

@api_view(['POST'])
def create_shipment(request):
    serializer = ShipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_shipments(request):
    shipments = Shipment.objects.all()
    serializer = ShipmentSerializer(shipments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_shipment_detail(request, shipmentId):
    try:
        shipment = Shipment.objects.get(shipmentId=shipmentId)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Shipment.DoesNotExist:
        return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_shipment(request, shipmentId):
    try:
        shipment = Shipment.objects.get(shipmentId=shipmentId)
        serializer = ShipmentSerializer(shipment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Shipment.DoesNotExist:
        return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_shipment(request, shipmentId):
    try:
        shipment = Shipment.objects.get(shipmentId=shipmentId)
        shipment.delete()
        return Response({"message": "Shipment deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Shipment.DoesNotExist:
        return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)