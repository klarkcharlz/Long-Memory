from django.contrib import admin

from .models import Notifications


class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('user_id',
                    'title',
                    'description',
                    'created_at',
                    'next_notifications',
                    'is_active')
    list_display_links = ('title', )
    search_fields = ('title', 'description')
    list_filter = ('user_id', 'created_at')  # фильтрация


admin.site.register(Notifications, NotificationsAdmin)
