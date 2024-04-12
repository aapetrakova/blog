from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserPost(models.Model):
    h1 = models.CharField(default='', max_length=200)
    title = models.CharField(verbose_name='Заголовок', default='', max_length=200)
    url = models.SlugField(verbose_name='URL')
    description = RichTextUploadingField(verbose_name='Описание поста')
    content = RichTextUploadingField(verbose_name='Текст поста')
    image = models.ImageField(verbose_name='Изображение', default='default.jpeg', upload_to='images/posts_images/%Y/%m/%d')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager(verbose_name='Теги', blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    image = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/avatars/%Y/%m/%d/',
        default='images/default_profile.jpg',
        blank=True)
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user.username

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):

        instance.profile.save()
