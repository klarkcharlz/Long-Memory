import requests
from pprint import pprint


class LongMemoryAPI:
    REG_URL = "http://{}/api/register/"
    AUTH_URL = 'http://{}/api-custom-auth/'

    def __init__(self, host: str):
        self.host = host
        self.session = requests.Session()
        self.token = None

    def _save_token(self, token):
        if token and not self.token:
            self.session.headers.update({'Authorization': f'token {token}'})
            self.token = token

    def registration(self, login, password, email):
        url = self.REG_URL.format(self.host)
        data = {
            "username": login,
            "password": password,
            "email": email
        }
        response = self.session.post(url, json=data)
        token = response.json().get('token')
        self._save_token(token)
        return response.status_code, response.json()

    def authorization(self, login, password):
        url = self.AUTH_URL.format(self.host)
        data = {
            "username": login,
            "password": password,
        }
        response = self.session.post(url, json=data)
        token = response.json().get('token')
        self._save_token(token)
        return response.status_code, response.json()


if __name__ == "__main__":
    HOST = '127.0.0.1:8000'
    test_api = LongMemoryAPI(HOST)
    # pprint(test_api.registration('tester', 'tester', 'tester@tester.ru'))
    pprint(test_api.authorization('tester', 'tester'))
