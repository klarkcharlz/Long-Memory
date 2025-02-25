from datetime import datetime

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import NotificationsSerializer, ThemeSerializer
from .models import Notifications, Theme


class NotificationsListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user_id'] = request.user.id  # Устанавливаем user_id из request.user

        # Если theme передаётся, убедимся, что она принадлежит текущему пользователю
        if 'theme' in data:
            theme_id = data['theme']
            try:
                theme = Theme.objects.get(id=theme_id, user=request.user)
                data['theme'] = theme.id
            except Theme.DoesNotExist:
                data['theme'] = None  # Если тема не найдена или не принадлежит пользователю

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """Возвращает все напоминания для авторизованного пользователя."""
        user = self.request.user
        return Notifications.objects.filter(
            user_id=user, is_active=True,
            next_notifications__lte=datetime.now()
        ).order_by('next_notifications')


class NotificationsDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    def get_queryset(self):
        user = self.request.user
        return Notifications.objects.filter(user_id=user, is_active=True)

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

    def put(self, request, *args, **kwargs):
        data = request.data
        notify = self.get_object()

        if request.user.id != notify.user_id.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        notify.title = data.get('title', notify.title)
        notify.description = data.get('description', notify.description)

        # Обновляем тему, если передана
        theme_id = data.get('theme')
        if theme_id is not None:
            try:
                theme = Theme.objects.get(id=theme_id, user=request.user)
                notify.theme = theme
            except Theme.DoesNotExist:
                return Response({"error": "Тема не найдена или не принадлежит пользователю"},
                                status=status.HTTP_400_BAD_REQUEST)

        notify.save()
        return self.retrieve(request, *args, **kwargs)


class ThemeListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThemeSerializer

    def get_queryset(self):
        """Возвращает все темы для авторизованного пользователя."""
        user = self.request.user
        return Theme.objects.filter(user=user).order_by('title')

    def perform_create(self, serializer):
        """Автоматически устанавливает текущего пользователя при создании темы."""
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """Переопределяем метод create для кастомного ответа."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ThemeDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ThemeSerializer
    lookup_field = 'id'  # Поле для поиска темы

    def get_queryset(self):
        """Возвращает только те темы, которые принадлежат текущему пользователю."""
        user = self.request.user
        return Theme.objects.filter(user=user)
