from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from bson import ObjectId

# Kết nối MongoDB
db = settings.MONGO_DB
books_collection = db["books"]  # Collection chuyên biệt cho sách
items_collection = db["items"]  # Collection chứa tất cả sản phẩm

def add_book(title, author, price, genre, published_year, image_url=None):
    """
    Thêm sách vào MongoDB, hỗ trợ lưu link ảnh (không upload file)
    """
    if not title or not author or not price:
        return JsonResponse({"status": "error", "message": "Thiếu thông tin bắt buộc"}, status=400)
    
    book_data = {
        "title": title,
        "author": author,
        "price": price,
        "genre": genre,
        "published_year": published_year,
        "image": image_url,  # Lưu đường dẫn ảnh trực tuyến
        "created_at": datetime.utcnow()
    }

    # Lưu vào MongoDB (books)
    result = books_collection.insert_one(book_data)
    book_data["_id"] = str(result.inserted_id)

    # Lưu vào MongoDB (items) để quản lý chung
    item_data = {
        "_id": book_data["_id"],  # Dùng chung ID giữa books & items
        "name": title,
        "category": "book",
        "price": price,
        "created_at": book_data["created_at"],
        "image": image_url,  # Đường dẫn ảnh trong collection items
        "details": {
            "author": author,
            "genre": genre,
            "published_year": published_year
        }
    }
    items_collection.insert_one(item_data)

    return JsonResponse({"status": "success", "data": book_data}, status=201)

def get_book_by_id(book_id):
    """
    Lấy thông tin sách theo book_id
    """
    try:
        book = books_collection.find_one({"_id": ObjectId(book_id)})
        if not book:
            return JsonResponse({"status": "error", "message": "Không tìm thấy sách"}, status=404)

        book["_id"] = str(book["_id"])
        return JsonResponse({"status": "success", "data": book}, status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


def get_all_books():
    """
    Lấy danh sách tất cả sách
    """
    books = list(books_collection.find({}))
    
    if not books:
        return JsonResponse({"status": "error", "message": "Không có sách nào"}, status=404)

    # Chuyển ObjectId sang string
    for book in books:
        book["_id"] = str(book["_id"])

    return JsonResponse({"status": "success", "data": books}, status=200)


def update_book(book_id, updated_data):
    """
    Cập nhật thông tin sách trong cả books & items
    """
    try:
        result = books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": updated_data})
        if result.matched_count == 0:
            return JsonResponse({"status": "error", "message": "Không tìm thấy sách để cập nhật"}, status=404)

        # Cập nhật trong items nếu tồn tại
        items_collection.update_one({"_id": book_id}, {"$set": {"details": updated_data}}, upsert=True)

        return JsonResponse({"status": "success", "message": "Cập nhật sách thành công"}, status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


def delete_book(book_id):
    """
    Xóa sách trong cả books & items
    """
    try:
        result = books_collection.delete_one({"_id": ObjectId(book_id)})
        if result.deleted_count == 0:
            return JsonResponse({"status": "error", "message": "Không tìm thấy sách để xóa"}, status=404)

        # Xóa khỏi items nếu tồn tại
        items_collection.delete_one({"_id": book_id})

        return JsonResponse({"status": "success", "message": "Xóa sách thành công"}, status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
