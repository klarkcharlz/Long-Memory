from datetime import datetime

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import NotificationsSerializer
from .models import Notifications


class NotificationsListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user_id'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Возвращает все напоминания для авторизованного пользователя, происходит выборка записей по полям:
            user_id - это user полученный из request.user,
            is_active - активное напоминание, должно быть True, если напоминание больше не актуально - False,
            next_notifications -  все актуальные напоминания на текущее время
        """
        user = self.request.user
        return Notifications.objects.filter(user_id=user, is_active=True, next_notifications__gte=datetime.now())


class NotificationsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
