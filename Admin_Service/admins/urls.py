from django.urls import path
from .views import create_admin, get_all_admins, get_admin_detail, update_admin, delete_admin

urlpatterns = [
    path('admins/', create_admin, name='create_admin'),
    path('admins/all/', get_all_admins, name='get_all_admins'),
    path('admins/<str:adminId>/', get_admin_detail, name='get_admin_detail'),
    path('admins/<str:adminId>/update/', update_admin, name='update_admin'),
    path('admins/<str:adminId>/delete/', delete_admin, name='delete_admin'),
]