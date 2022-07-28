from datetime import datetime, timedelta

from django.db import models

from users.models import CustomUser


class Notifications(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    period_type = models.SmallIntegerField(default=0)
    next_notifications = models.DateTimeField(verbose_name="Дата следующего напоминания",
                                              default=datetime.utcnow() + timedelta(days=1))
    is_active = models.BooleanField(verbose_name="Описание", default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f"{self.title}: {self.description[:20]}"

    def calculate_first_notification_date(self):
        self.next_notifications = datetime.utcnow() + timedelta(days=1)
