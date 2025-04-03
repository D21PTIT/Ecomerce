from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import Customer
import json

@csrf_exempt
def register_customer(request):
    """API Đăng ký tài khoản"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            email = data.get("email")
            phone = data.get("phone")
            password = data.get("password")  # Không hash mật khẩu
            address = data.get("address")

            # Kiểm tra nếu email hoặc số điện thoại đã tồn tại
            if Customer.objects.filter(email=email).exists():
                return JsonResponse({"status": "error", "message": "Email đã tồn tại"}, status=400)
            if Customer.objects.filter(phone=phone).exists():
                return JsonResponse({"status": "error", "message": "Số điện thoại đã tồn tại"}, status=400)

            # Tạo khách hàng mới
            customer = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,  # Lưu plain text
                address=address
            )

            return JsonResponse({
                "status": "success",
                "message": "Đăng ký thành công",
                "customer_id": customer.id
            }, status=201)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)


@csrf_exempt
def login_customer(request):
    """API Đăng nhập tài khoản"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            # Kiểm tra email và mật khẩu
            customer = Customer.objects.filter(email=email, password=password).first()
            if customer:
                return JsonResponse({
                    "status": "success",
                    "message": "Đăng nhập thành công",
                    "customer_id": customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "email": customer.email
                }, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Sai email hoặc mật khẩu"}, status=401)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Only POST method allowed"}, status=405)
