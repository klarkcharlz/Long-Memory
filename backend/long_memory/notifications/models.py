from datetime import datetime, timedelta

from django.db import models

from users.models import CustomUser
from .constants import TIME_DELTA_MAP


def utc_tomorrow():
    return datetime.utcnow() + timedelta(days=1)


class Theme(models.Model):
    class Meta:
        verbose_name = 'Тема напоминания'
        verbose_name_plural = 'Темы напоминания'

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='themes'
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return self.title


class Notifications(models.Model):
    class Meta:
        verbose_name = 'Напоминания'
        verbose_name_plural = 'Напоминания'

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    period_type = models.SmallIntegerField(default=0)
    next_notifications = models.DateTimeField(verbose_name="Дата следующего напоминания",
                                              default=utc_tomorrow)
    is_active = models.BooleanField(verbose_name="Активное напоминание", default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    theme = models.ForeignKey(
        Theme, on_delete=models.SET_NULL, verbose_name='Тема',
        related_name='theme', null=True, default=None
    )

    def __str__(self):
        return f"{self.user_id} -  {self.title}: {self.description[:20]}"

    def calculate_next_notification_date(self):
        if self.period_type < 6:
            self.period_type += 1
        self.next_notifications = datetime.utcnow() + TIME_DELTA_MAP[self.period_type]
