from rest_framework import serializers
from .models import Notifications


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id', 'user_id', 'title', 'description', 'created_at', 'next_notifications']
