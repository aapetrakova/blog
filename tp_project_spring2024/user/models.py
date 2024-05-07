from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class UserPost(models.Model):
    """
    Model for storing user posts

    atribute:h1: CharField - h1 title of post
    atribute:title: CharField - the title of post
    atribute:url: SlugField - the url of post
    atribute:description: RichTextField - the description of post
    atribute:content: RichTextField - the content of post
    atribute:image: ImageField - image for post
    atribute:created_at: DateTimeField - date and time when the comment was created
    atribute:author: User - author of post
    """
    h1 = models.CharField(default='', max_length=200)
    title = models.CharField(default='', max_length=200)
    url = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField(default='default.jpeg', upload_to='images')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
