from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import BugReportSerializer
from .models import BugReport


class BugReportCreateView(generics.CreateAPIView):
    model = BugReport
    serializer_class = BugReportSerializer
    queryset = BugReport.objects.all()

    def create(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        data = request.data
        data['ip_address'] = ip
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
