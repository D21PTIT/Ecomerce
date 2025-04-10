from django.db import models

class Comment(models.Model):
    commentId = models.CharField(max_length=50, primary_key=True)
    itemId = models.CharField(max_length=50)
    customerId = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
    commentDate = models.DateTimeField(auto_now_add=True)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment {self.commentId} for Item {self.itemId} by Customer {self.customerId}"