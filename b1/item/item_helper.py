from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from bson import ObjectId

# Kết nối MongoDB
db = settings.MONGO_DB
items_collection = db["items"]  # Collection chứa tất cả sản phẩm

def add_item(name, category, price, details):
    """
    Thêm sản phẩm mới vào collection items
    """
    if not name or not category or not price:
        return JsonResponse({"status": "error", "message": "Thiếu thông tin bắt buộc"}, status=400)
    
    item = {
        "name": name,
        "category": category,
        "price": price,
        "created_at": datetime.utcnow(),
        "details": details  # Thông tin riêng của từng loại sản phẩm
    }

    # Lưu vào MongoDB
    result = items_collection.insert_one(item)
    item["_id"] = str(result.inserted_id)

    return JsonResponse({"status": "success", "data": item}, status=201)


def get_item_by_id(item_id):
    """
    Lấy thông tin sản phẩm theo item_id
    """
    try:
        item = items_collection.find_one({"_id": ObjectId(item_id)})
        if not item:
            return JsonResponse({"status": "error", "message": "Không tìm thấy sản phẩm"}, status=404)

        item["_id"] = str(item["_id"])  # Chuyển ObjectId thành string
        return JsonResponse({"status": "success", "data": item}, status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


def get_items_by_category(category):
    """
    Lấy danh sách sản phẩm theo category (book, phone, laptop)
    """
    items = list(items_collection.find({"category": category}))
    
    if not items:
        return JsonResponse({"status": "error", "message": "Không tìm thấy sản phẩm"}, status=404)

    # Chuyển ObjectId sang string
    for item in items:
        item["_id"] = str(item["_id"])

    return JsonResponse({"status": "success", "data": items}, status=200)
