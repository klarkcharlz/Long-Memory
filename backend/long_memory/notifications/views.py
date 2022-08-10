from datetime import datetime

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import NotificationsSerializer
from .models import Notifications


class NotificationsListCreateView(generics.ListCreateAPIView):
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
        return Notifications.objects.filter(user_id=user, is_active=True,
                                            next_notifications__lte=datetime.now()).order_by('next_notifications')


class NotificationsDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    def get_queryset(self):
        user = self.request.user
        return Notifications.objects.filter(user_id=user,
                                            is_active=True,
                                            next_notifications__gte=datetime.now())

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id == instance.user_id.id:
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        """ Метод path обновляет время следующего напоминания. Меняет дату и время в поле next_next_notifications
         а так же period_type
        """
        notify = Notifications.objects.get(pk=kwargs['pk'])
        if request.user.id == notify.user_id.id:
            notify.calculate_next_notification_date()
            notify.save()
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
