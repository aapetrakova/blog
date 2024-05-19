from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from user.models import UserPost


class Comment(models.Model):
    """Model of a comment

    atribute:post: UserPost - post to which the comment is attached
    atribute:username: User - username of the user
    atribute:text: TextField - text of the comment
    atribute:created_date: DateTimeField - date and time when the comment was created
    """

    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
