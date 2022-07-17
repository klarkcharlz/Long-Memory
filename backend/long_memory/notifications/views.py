from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import NotificationsSerializer
from .models import Notifications


class NotificationsViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
                           ):
    permission_classes = [DjangoModelPermissions]
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        print(request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            print('tut')
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
