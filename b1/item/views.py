from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .item_helper import add_item, get_item_by_id, get_items_by_category

@csrf_exempt
def add_item_view(request):
    """API thêm item vào MongoDB"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            category = data.get("category")
            price = data.get("price")
            details = data.get("details", {})

            return add_item(name, category, price, details)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


def get_item_view(request, item_id):
    """API lấy thông tin sản phẩm theo item_id"""
    return get_item_by_id(item_id)


def get_items_view(request, category):
    """API lấy danh sách sản phẩm theo category"""
    return get_items_by_category(category)
