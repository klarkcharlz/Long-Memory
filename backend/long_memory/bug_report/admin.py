from django.contrib import admin

from .models import BugReport


class BugReportAdmin(admin.ModelAdmin):
    list_display = ('user_name',
                    'ip_address',
                    'short_description',
                    'is_active',
                    'created_at',
                    )
    list_display_links = ('short_description', )
    list_filter = ('is_active', 'ip_address')


admin.site.register(BugReport, BugReportAdmin)
