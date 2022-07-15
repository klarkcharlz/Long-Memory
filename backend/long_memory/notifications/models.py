from datetime import datetime, timedelta

from django.db import models

from users.models import CustomUser


def calculate_first_notification_date():
    return datetime.now() + timedelta(days=1)


class Notifications(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    period_type = models.SmallIntegerField(default=0)
    next_notifications = models.DateTimeField(verbose_name="Дата следующего напоминания",
                                              default=calculate_first_notification_date())
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f"{self.title}: {self.description[:20]}"
