from datetime import datetime

from rest_framework import generics, permissions


from .serializers import NotificationsSerializer
from .models import Notifications


class NotificationsListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

    def get_queryset(self):
        """Возвращает все напоминания для авторизованного пользователя, происходит выборка записей по полям:
            user_id - это user полученный из request.user,
            is_active - активное напоминание, должно быть True, если напоминание больше не актуально - False,
            next_notifications -  все актуальные напоминания на текущее время
        """
        user = self.request.user
        return Notifications.objects.filter(user_id=user, is_active=True, next_notifications__gte=datetime.now())


class NotificationsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

    def patch(self, request, *args, **kwargs):
        """ Метод patch переопределен для изменения поля is_active, по умолчанию при создании напоминания is_active
            присвоено True, когда пользователи решил, что это напоминание больше не нужно показывать, то нужно is_active
            присвоить False. Механизм следующий: с front-end должно прийти id напоминания через url,
            например:
                метод PATCH,  http://host/notifications/id/
        """
        notify = Notifications.objects.get(pk=kwargs['pk'])
        notify.is_active = False
        notify.save()
        return self.partial_update(request, *args, **kwargs)

