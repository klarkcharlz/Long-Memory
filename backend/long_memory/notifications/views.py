from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets

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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
