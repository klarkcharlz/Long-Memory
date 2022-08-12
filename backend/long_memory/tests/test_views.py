from .test_setup import TestSetUp


class TestView(TestSetUp):

    def test_admin_page(self):
        res = self.client.get(self.admin_url)
        self.assertEqual(res.status_code, 200)

    def test_admin_page_login(self):
        res = self.client.post(self.admin_url, self.admin_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_admin_page_no_login(self):
        res = self.client.post(self.admin_url)
        self.assertIsNot(res.status_code, 400)

    def test_api_page(self):
        res = self.client.get(self.api_url)
        self.assertEqual(res.status_code, 200)

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertIsNot(res.status_code, 400)

    def test_user_can_register_page(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()

        # res = self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_no_data(self):
        res = self.client.post(self.auth_url)
        self.assertIsNot(res.status_code, 400)

    def test_can_access_page_login(self):
        res = self.client.get(self.auth_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_not_access_page_notifications(self):
        res = self.client.post(self.notifications_url)
        self.assertIsNot(res.status_code, 400)

    def test_not_access_page_user_data(self):
        res = self.client.post(self.user_data_url)
        self.assertIsNot(res.status_code, 400)