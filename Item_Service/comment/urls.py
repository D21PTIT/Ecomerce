from django.urls import path
from .views import create_comment, get_comments_by_item, get_all_comments, classify_comment

urlpatterns = [
    path('', create_comment, name='create_comment'),  # /api/comments/
    path('item/<str:itemId>/', get_comments_by_item, name='get_comments_by_item'),  # /api/comments/item/{itemId}/
    path('all/', get_all_comments, name='get_all_comments'),  # /api/comments/all/
    path('classify/<str:commentId>/', classify_comment, name='classify_comment'),

]