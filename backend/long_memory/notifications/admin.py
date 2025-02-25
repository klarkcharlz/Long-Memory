from django.contrib import admin

from .models import Notifications, Theme


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


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    list_display_links = ('title', )
    search_fields = ('user', 'title')
    list_filter = ('user', 'title',)  # фильтрация


admin.site.register(Theme, ThemesAdmin)
