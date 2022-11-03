from typing import Dict, List
from pprint import pprint

from fastapi import WebSocket
from httpx import AsyncClient, Response

from logger import logger
from settings import ADMIN_CHAT

USED_CHAT_IDS = []


def get_free_chat_id() -> int:
    i = 1
    while True:
        if i not in USED_CHAT_IDS:
            USED_CHAT_IDS.append(i)
            break
        i += 1
    return i


class Bot:

    def __init__(self, token: str, admin_chat_id: int, skip_updates: bool = False):
        self.token = token
        self.admin_chat_id = admin_chat_id
        self.offset = 0

        self.state = {
            'chat_id': None
        }

        self.skip_updates = skip_updates

    def get_url(self, method: str) -> str:
        return f"https://api.telegram.org/bot{self.token}/{method}"

    @staticmethod
    async def post_request(url: str, payload: dict) -> Response:
        async with AsyncClient() as client:
            request = await client.post(url, json=payload)
            return request

    @staticmethod
    async def get_request(url: str, params: dict) -> Response:
        async with AsyncClient() as client:
            request = await client.get(url, params=params)
            return request

    async def send_message_to_admin_chat(self, message: dict, chat_id: int) -> None:
        url = self.get_url("sendMessage")

        user = message['name']
        text = message['message']
        message = f"User {user}\nChat id №{chat_id}\n{text}"

        payload = {
            'chat_id': self.admin_chat_id,
            'text': message,
            'reply_markup': {
                "inline_keyboard": [[{'text': 'Ответить', 'callback_data': f'Answer {chat_id}'}]],
            }
        }
        req = await self.post_request(url, payload)
        status_code = req.status_code
        if status_code != 200:
            logger.error(req.text)
            logger.error(f"Status code send message to telegram != 200({status_code}).")

    async def get_updates(self, timeout: int = 0) -> List[Dict]:
        url = self.get_url("getUpdates")
        params = {'offset': self.offset}
        if timeout:
            params['timeout'] = timeout

        req = await self.get_request(url, params)
        status_code = req.status_code
        if status_code != 200:
            logger.error(req.text)
            logger.error(f"Status code update telegram != 200({status_code}).")

        data = req.json()

        answers = []

        if not self.skip_updates:
            for mes_obj in data['result']:
                self.offset = mes_obj['update_id'] + 1
                if 'message' in mes_obj:
                    answer = self.parse_admin_response(mes_obj)
                    if answer:
                        if isinstance(answer, dict):
                            answers.append(answer)
                        if isinstance(answer, str):
                            answers.append({
                                'chat_id': self.state['chat_id'],
                                'text': answer
                            })
                elif 'callback_query' in mes_obj:
                    callback_data = mes_obj['callback_query']['message']['reply_markup']['inline_keyboard'][0][0][
                        'callback_data']
                    self.state['chat_id'] = int(callback_data.split()[1])
        else:
            # при первом запуске ничего не делаем, просто считаем offset
            for mes_obj in data['result']:
                self.offset = mes_obj['update_id'] + 1

        self.skip_updates = False
        return answers

    @staticmethod
    def parse_admin_response(mes_obj: dict):
        user_id = mes_obj['message']['chat']['id']
        if user_id == ADMIN_CHAT:
            answer: str = mes_obj['message']['text']
            if answer.startswith('/answer'):
                # вариант с командой
                try:
                    _, chat_id, *text = answer.split()
                    chat_id = int(chat_id)
                    text = " ".join(text)
                    if chat_id and text:
                        # logger.info(f"Сообщение для чата №{chat_id}: {text}")
                        return {
                            'chat_id': chat_id,
                            'text': text
                        }
                except ValueError as err:
                    logger.exception(err)
                    logger.error('АДМИН СКАЗАЛ ФИГНЮ!')
            else:
                # просто сбор сообщений, будет проверяться стейт
                return answer
        else:
            first_name = mes_obj['message']['chat']['first_name']
            last_name = mes_obj['message']['chat']['last_name']
            username = mes_obj['message']['chat']['username']
            logger.warning(f'Посторонний! {user_id}: {username}: {first_name} {last_name}')


class User:
    def __init__(self, name: str, client_id: str, websocket: WebSocket):
        self.name = name
        self.client_id = client_id
        self.websocket = websocket
        self.chat_id: int = get_free_chat_id()
        self.first_message = False

    def __str__(self):
        return f"{self.name}: {self.client_id}"

    def __repr__(self):
        return f"{self.name}: {self.client_id}"


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int: User] = {}

    async def connect(self, websocket: WebSocket, name: str, client_id: str) -> int:
        await websocket.accept()
        user = User(name, client_id, websocket)
        self.active_connections[user.chat_id] = user
        return user.chat_id

    def disconnect(self, websocket: WebSocket) -> None:
        for chat_id, user in self.active_connections.copy().items():
            if user.websocket == websocket:
                USED_CHAT_IDS.remove(chat_id)
                logger.warning(f'user chat id №{chat_id} disconnect')
                del self.active_connections[chat_id]

    async def send_personal_message(self, message: str, chat_id: int) -> None:
        await self.active_connections[chat_id].websocket.send_text(message)

    async def broadcast(self, message: str) -> None:
        for client_id, user in self.active_connections.items():
            await user.websocket.send_text(message)
