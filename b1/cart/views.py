from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .cart_helper import create_cart, get_cart_by_user

@csrf_exempt
def create_cart_view(request):
    """API tạo giỏ hàng mới"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            books = data.get("books", [])

            return create_cart(user_id, books)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


def get_cart_view(request, user_id):
    """API lấy giỏ hàng theo user_id"""
    return get_cart_by_user(user_id)
