from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from users.models import CustomUser


class ChekUser(APITestCase):

    url = "/admin/"
    username = 'admin'
    password = '12345'

    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user(
            username = self.username,
            password = self.password,
        )
        self.client = APIClient()


    def test_auth(self):

        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

