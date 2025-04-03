from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customer.urls')),  # Chuyển toàn bộ routes của `customer` vào `customer/urls.py`
    path('book/', include('book.urls')),
    path('cart/', include('cart.urls')),
    path('item/', include('item.urls'))
]



