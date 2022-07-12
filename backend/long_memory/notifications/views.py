from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets

from .serializers import NotificationsSerializer
from .models import Notifications


class NotificationsViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
                           ):
    permission_classes = [DjangoModelPermissions]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
