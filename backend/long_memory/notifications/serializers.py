from rest_framework import serializers
from .models import Notifications, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'title', 'user']
        read_only_fields = ['user']


class NotificationsSerializer(serializers.ModelSerializer):
    theme = serializers.PrimaryKeyRelatedField(
        queryset=Theme.objects.all(), required=False, write_only=True
    )
    theme_data = ThemeSerializer(source='theme', read_only=True)  # Для чтения вложенный объект

    class Meta:
        model = Notifications
        fields = [
            'id', 'user_id', 'title', 'description', 'created_at',
            'next_notifications', 'theme', 'theme_data'
        ]
