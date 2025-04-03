from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from bson import ObjectId
from customer.models import Customer

# Kết nối đến MongoDB
db = settings.MONGO_DB
carts_collection = db["carts"]

def create_cart(user_id, books):
    """
    Tạo giỏ hàng mới với user_id và danh sách sách
    """
    if not user_id :
        return JsonResponse({"status": "error", "message": "user_id và books là bắt buộc"}, status=400)

    # Kiểm tra danh sách books
    for book in books:
        if 'book_id' not in book or 'quantity' not in book:
            return JsonResponse({"status": "error", "message": "Mỗi sách cần có book_id và quantity"}, status=400)

    # Tạo giỏ hàng
    cart = {
        "user_id": user_id,
        "books": books,
        "created_at": datetime.utcnow()
    }

    # Lưu vào MongoDB
    result = carts_collection.insert_one(cart)
    cart["_id"] = str(result.inserted_id)

    return JsonResponse({"status": "success", "data": cart}, status=201)


def get_cart_by_user(user_id):
    """
    Lấy giỏ hàng theo user_id
    """
    # Kiểm tra user_id có tồn tại trong MySQL không
    if not Customer.objects.filter(id=user_id).exists():
        return JsonResponse({"status": "error", "message": "User không tồn tại trong hệ thống"}, status=404)

    # Lấy giỏ hàng từ MongoDB
    cart = carts_collection.find_one({"user_id": user_id})
    
    if cart:
        cart["_id"] = str(cart["_id"])  # Chuyển ObjectId thành chuỗi
        return JsonResponse({"status": "success", "data": cart}, status=200)
    
    return JsonResponse({"status": "error", "message": "Không tìm thấy giỏ hàng cho user này"}, status=404)
