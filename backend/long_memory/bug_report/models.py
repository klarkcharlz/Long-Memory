from django.db import models
from django.template.defaultfilters import truncatechars


class BugReport(models.Model):
    class Meta:
        verbose_name = 'Баг Репорт'
        verbose_name_plural = 'Баг Репорты'

    user_name = models.CharField(max_length=64, verbose_name="Имя")
    ip_address = models.CharField(max_length=64, verbose_name="IP", blank=True)
    contacts = models.TextField(verbose_name="Контакты", blank=True)
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(verbose_name="Активный репорт", default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.user_name}: {self.description[1:20]}"

    @property
    def short_description(self):
        return truncatechars(self.description, 60)
