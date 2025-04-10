from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('item.urls')),
    path('api/comments/', include('comment.urls')),  # Thêm /api/
]