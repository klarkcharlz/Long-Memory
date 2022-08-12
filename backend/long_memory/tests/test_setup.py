from rest_framework.test import APITestCase

class TestSetUp(APITestCase):

    def setUp(self):
        self.admin_url = 'http://127.0.0.1:8000/admin/login/'
        self.api_url = 'http://127.0.0.1:8000/api/'
        self.register_url = 'http://127.0.0.1:8000/api/register/'
        self.auth_url = 'http://127.0.0.1:8000/api-auth/login/'
        self.notifications_url = 'http://127.0.0.1:8000/api/notifications/'
        self.user_data_url = 'http://127.0.0.1:8000/api/user_data/'

        self.user_data={
            'username': "admin",
            'password': "12345",
            'email': "email@email.ru",
        }

        self.admin_data={
            'username': "admin",
            'password': "1234",
        }

        self.notifications_data = {
            'user_id': "admin",
            'title': "test_title",
            'description': "test test test",
            'created_at': "11.08.2023 17.17",
            'next_notifications': "null",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

