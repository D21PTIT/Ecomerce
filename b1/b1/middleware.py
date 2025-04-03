# middleware.py

class SimpleCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Thêm CORS headers
        response["Access-Control-Allow-Origin"] = "*"  # Hoặc chỉ định domain cụ thể như "http://localhost:3000"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

        # Đáp ứng yêu cầu preflight (OPTIONS)
        if request.method == "OPTIONS":
            response.status_code = 200

        return response
