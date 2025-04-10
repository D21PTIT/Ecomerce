from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('admins.urls')),  # Sửa từ admin_service_app thành admins
]