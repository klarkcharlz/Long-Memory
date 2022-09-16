from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .serializers import CreateUserSerializer, UserSerializer
from .models import CustomUser


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CreateUserSerializer
    queryset = CustomUser.objects.all()

    activation_link = '{}/activate/{}/{}'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_id = serializer.instance.id
        confirmation_token = default_token_generator.make_token(serializer.instance)
        link = self.activation_link.format(settings.DOMAIN_NAME, user_id, confirmation_token)
        msg_html = render_to_string('email.html', {'link': link})
        subject, from_email, to = 'Email Verification', 'Long Memory App', serializer.instance.email
        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(msg_html, "text/html")
        msg.send()
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'done'}, status=status.HTTP_201_CREATED, headers=headers)


class UserView(RetrieveUpdateAPIView):
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.request.user.id
        queryset = CustomUser.objects.filter(pk=user_id)
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


@action(detail=False, permission_classes=[AllowAny], methods=['get'])
def activate_user(request, uid, token):
    response = HttpResponse()
    try:
        user = CustomUser.objects.filter(pk=uid, is_active=False).first()
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if not user:
        response.content = 'User not found'
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response
    if not default_token_generator.check_token(user, token):
        response.content = 'Token is invalid or expired. Please request another confirmation email by signing in.'
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response
    user.is_active = True
    user.save()
    Token.objects.get_or_create(user=user)
    response.content = 'Email successfully confirmed'
    response.status_code = status.HTTP_201_CREATED
    return response
