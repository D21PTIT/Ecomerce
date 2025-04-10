from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
import pickle
import os
from pathlib import Path

# Tải mô hình đã huấn luyện
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'sentiment_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    sentiment_model = pickle.load(f)

# Hàm tiền xử lý văn bản (nếu cần)
def preprocess_text(text):
    # Chuyển thành chữ thường
    text = text.lower()
    # Thêm các bước tiền xử lý khác nếu cần
    return text

@api_view(['POST'])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_comments_by_item(request, itemId):
    comments = Comment.objects.filter(itemId=itemId)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# API mới để phân loại bình luận
@api_view(['GET'])
def classify_comment(request, commentId):
    try:
        # Lấy bình luận theo commentId
        comment = Comment.objects.get(commentId=commentId)
    except Comment.DoesNotExist:
        return Response({"error": "Không tìm thấy bình luận"}, status=status.HTTP_404_NOT_FOUND)

    # Tiền xử lý nội dung bình luận
    content = preprocess_text(comment.content)

    # Dự đoán cảm xúc
    prediction = sentiment_model.predict([content])[0]
    sentiment = prediction  # Đã là "tích cực" hoặc "tiêu cực"

    # Trả về kết quả
    return Response({
        "commentId": comment.commentId,
        "content": comment.content,
        "sentiment": sentiment
    }, status=status.HTTP_200_OK)