from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .book_helper import add_book, get_book_by_id, get_all_books, update_book, delete_book

@csrf_exempt
def add_book_view(request):
    """API thêm sách vào MongoDB, chỉ lưu link ảnh"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            author = data.get("author")
            price = data.get("price")
            genre = data.get("genre")
            published_year = data.get("published_year")
            image_url = data.get("image_url")  # Nhận URL ảnh từ request

            return add_book(title, author, price, genre, published_year, image_url)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


def get_book_view(request, book_id):
    """API lấy thông tin sách theo book_id"""
    return get_book_by_id(book_id)


def get_all_books_view(request):
    """API lấy danh sách tất cả sách"""
    return get_all_books()


@csrf_exempt
def update_book_view(request, book_id):
    """API cập nhật thông tin sách"""
    if request.method == "PUT":
        try:
            updated_data = json.loads(request.body)
            return update_book(book_id, updated_data)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only PUT method allowed"}, status=405)


@csrf_exempt
def delete_book_view(request, book_id):
    """API xóa sách"""
    if request.method == "DELETE":
        return delete_book(book_id)

    return JsonResponse({"status": "error", "message": "Only DELETE method allowed"}, status=405)
