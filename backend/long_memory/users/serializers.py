from rest_framework import serializers
from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )

        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
            "email",
        )


class UserSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField()

    class Meta:
        model = UserModel
        fields = (
            'username',
            'first_name',
            'email',
            'avatar',
            'telegram_id',
            'telegram_reminders',
            'vk_id',
            'vk_reminders',
            'email_reminders',
        )
