from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email address", unique=True)
    telegram_id = models.CharField(verbose_name='Telegram id', max_length=255, blank=True)
    vk_id = models.CharField(verbose_name='VK id', max_length=255, blank=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.username
