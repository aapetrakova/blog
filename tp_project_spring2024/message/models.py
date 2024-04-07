from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from user.models import UserPost


class Comment(models.Model):
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
