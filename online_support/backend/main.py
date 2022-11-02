"""
uvicorn main:app --reload --port 5000
"""
import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi_utils.tasks import repeat_every

from classes import ConnectionManager, Bot
from logger import logger
from settings import TG_TOKEN, ADMIN_CHAT


app = FastAPI()
manager = ConnectionManager()
bot = Bot(TG_TOKEN, ADMIN_CHAT)


@app.on_event("startup")
@repeat_every(seconds=2, wait_first=True)
async def check_update():
    logger.info('check_update...')
    answers = await bot.get_updates(timeout=60)
    if answers:
        logger.info(f'Admin answers:\n{answers}')
        for answer in answers:
            if isinstance(answer, dict):
                chat_id = answer['chat_id']
                if chat_id in manager.active_connections:
                    text = answer['text']
                    # logger.info(f"Сообщение для чата №{chat_id}: {text}")
                    await manager.send_personal_message(text, chat_id)
            elif isinstance(answer, str):
                if bot.state['chat_id'] is not None:
                    await manager.send_personal_message(answer, bot.state['chat_id'])


@app.get("/")
async def get():
    return HTMLResponse('<h1>SUPPORT API</h1>')


@app.websocket("/ws/{name}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, name: str, client_id: str):
    chat_id = await manager.connect(websocket, name, client_id)
    logger.info(f'Current client cnt: {len(manager.active_connections)}.')
    logger.info(f'Active connections:\n{manager.active_connections}')
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            logger.info(f'{client_id} says: {data}')
            # await manager.send_personal_message(f"You says: {data}", client_id)  # ToDo echo
            await bot.send_message_to_admin_chat(data, chat_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
