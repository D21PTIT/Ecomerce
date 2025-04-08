from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item, Book, Laptop, Phone
from .serializers import ItemSerializer, BookSerializer, LaptopSerializer, PhoneSerializer

# API get all items với lọc và sắp xếp
@api_view(['GET'])
def get_all_items(request):
    # Lấy tất cả items (bao gồm Book, Laptop, Phone)
    books = Book.objects.all()
    laptops = Laptop.objects.all()
    phones = Phone.objects.all()

    # Kết hợp tất cả items
    all_items = list(books) + list(laptops) + list(phones)

    # Lọc theo category nếu có
    category = request.GET.get('category', None)
    if category:
        all_items = [item for item in all_items if item.category == category]

    # Sắp xếp theo sort (price hoặc createdDate)
    sort = request.GET.get('sort', None)
    if sort:
        if sort == 'price_asc':
            all_items = sorted(all_items, key=lambda x: x.price)
        elif sort == 'price_desc':
            all_items = sorted(all_items, key=lambda x: x.price, reverse=True)
        elif sort == 'date_asc':
            all_items = sorted(all_items, key=lambda x: x.createdDate)
        elif sort == 'date_desc':
            all_items = sorted(all_items, key=lambda x: x.createdDate, reverse=True)

    # Serialize dữ liệu
    serialized_items = []
    for item in all_items:
        if isinstance(item, Book):
            serializer = BookSerializer(item)
        elif isinstance(item, Laptop):
            serializer = LaptopSerializer(item)
        elif isinstance(item, Phone):
            serializer = PhoneSerializer(item)
        serialized_items.append(serializer.data)

    return Response(serialized_items, status=status.HTTP_200_OK)

# Các API khác (Book, Laptop, Phone) giữ nguyên
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_book_detail(request, itemId):
    try:
        book = Book.objects.get(itemId=itemId)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_book(request, itemId):
    try:
        book = Book.objects.get(itemId=itemId)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_book(request, itemId):
    try:
        book = Book.objects.get(itemId=itemId)
        book.delete()
        return Response({"message": "Book deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_laptop(request):
    serializer = LaptopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_laptops(request):
    laptops = Laptop.objects.all()
    serializer = LaptopSerializer(laptops, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_laptop_detail(request, itemId):
    try:
        laptop = Laptop.objects.get(itemId=itemId)
        serializer = LaptopSerializer(laptop)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Laptop.DoesNotExist:
        return Response({"error": "Laptop not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_laptop(request, itemId):
    try:
        laptop = Laptop.objects.get(itemId=itemId)
        serializer = LaptopSerializer(laptop, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Laptop.DoesNotExist:
        return Response({"error": "Laptop not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_laptop(request, itemId):
    try:
        laptop = Laptop.objects.get(itemId=itemId)
        laptop.delete()
        return Response({"message": "Laptop deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Laptop.DoesNotExist:
        return Response({"error": "Laptop not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_phone(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_phones(request):
    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_phone_detail(request, itemId):
    try:
        phone = Phone.objects.get(itemId=itemId)
        serializer = PhoneSerializer(phone)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_phone(request, itemId):
    try:
        phone = Phone.objects.get(itemId=itemId)
        serializer = PhoneSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_phone(request, itemId):
    try:
        phone = Phone.objects.get(itemId=itemId)
        phone.delete()
        return Response({"message": "Phone deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Phone.DoesNotExist:
        return Response({"error": "Phone not found"}, status=status.HTTP_404_NOT_FOUND)