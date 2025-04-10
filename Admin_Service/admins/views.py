from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Admin
from .serializers import AdminSerializer

@api_view(['POST'])
def create_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_admins(request):
    admins = Admin.objects.all()
    serializer = AdminSerializer(admins, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_admin_detail(request, adminId):
    try:
        admin = Admin.objects.get(adminId=adminId)
        serializer = AdminSerializer(admin)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Admin.DoesNotExist:
        return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_admin(request, adminId):
    try:
        admin = Admin.objects.get(adminId=adminId)
        serializer = AdminSerializer(admin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Admin.DoesNotExist:
        return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_admin(request, adminId):
    try:
        admin = Admin.objects.get(adminId=adminId)
        admin.delete()
        return Response({"message": "Admin deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Admin.DoesNotExist:
        return Response({"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND)