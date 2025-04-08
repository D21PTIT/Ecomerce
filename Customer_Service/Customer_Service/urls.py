# Customer_Service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customer.urls')),  # <- dòng này kết nối app
]
