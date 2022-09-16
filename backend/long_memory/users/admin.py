from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'telegram_id',
                    'vk_id',
                    'created_at',
                    'is_active')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_active', )


admin.site.register(CustomUser, CustomUserAdmin)
