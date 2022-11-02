import React, {useState} from 'react';
import {v4 as uuid} from 'uuid';


const name = 'client';

const wsConnect = () => {
    const client_id = uuid();
    const WS_URL = `ws://127.0.0.1:5000/ws/${name}/${client_id}`;
    const ws = new WebSocket(WS_URL);
    return [client_id, ws]
}

let [client_id, ws] = wsConnect();

const sendMessage = (data) => {
    ws.send(JSON.stringify(data));
}

let showAnswer;

ws.onmessage = (event) => {
    const receiveData = event.data;
    console.log(receiveData);
    showAnswer(receiveData);
};


const SupportChat = () => {
    const [name, setName] = useState('');
    const [message, setMessage] = useState('');
    const [answer, setAnswer] = useState('Ответ от сервера');

    showAnswer = setAnswer;

    return (
        <div>
            <form action="">
                <input type="text" placeholder='Ваше имя' value={name} onChange={
                    (e) => {
                        setName(e.target.value);
                    }
                }/>
                <br/>
                <input type="text" placeholder='Сообщение' value={message} onChange={
                    (e) => {
                        setMessage(e.target.value);
                    }
                }/>
                <br/>
                <button onClick={(e) => {
                    e.preventDefault();
                    if (name && message) {
                        const data = {
                            client_id,
                            name,
                            message
                        }
                        console.log(data);
                        sendMessage(data);
                    } else {
                        console.log('Empty data!')
                    }

                }}>Отправить
                </button>
            </form>
            <textarea name="text" id="" cols="30" rows="10" value={answer} readonly={true}></textarea>
        </div>
    );
};

export default SupportChat;