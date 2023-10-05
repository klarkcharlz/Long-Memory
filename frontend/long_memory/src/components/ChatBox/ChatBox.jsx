import React, {useState} from 'react';
import Message from '../Message/Message';
import {v4 as uuid} from 'uuid';

const testData = [
    {
        writer: 'user',
        text: 'Здарова'
    },
    {
        writer: 'admin',
        text: 'чо случилось'
    },
    {
        writer: 'user',
        text: 'твой сайт гавно'
    },
    {
        writer: 'admin',
        text: 'я знаю'
    },
]

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

function ChatBox() {
    const [name, setName] = useState('');
    const [message, setMessage] = useState('');
    const [answer, setAnswer] = useState('Ответ от сервера');

    showAnswer = setAnswer;

    return (
        <div style={{
            position: 'fixed',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            bottom: '60px',
            right: '20px',
            width: '300px',
            height: '400px',
            border: '2px solid #CFB82E',
            borderRadius: '10px',
            overflowY: 'scroll',
            backgroundColor: '#092754',
        }}>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                <input style={{
                    height: '25px',
                    borderTopLeftRadius: '10px',
                    borderTopRightRadius: '10px',
                    padding: '3px'
                }}
                       type="text"
                       placeholder='Ваше имя'
                       value={name}
                       onChange={
                           (e) => {
                               setName(e.target.value);
                           }
                       }/>
                />
            </div>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                {testData.map((msg, index) => {
                    return <Message writer={msg.writer} text={msg.text} key={index}/>
                })}
            </div>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                <input style={{
                    height: '25px',
                    padding: '3px'
                }}
                       type="text"
                       placeholder='Сообщение'
                       value={message}
                       onChange={
                           (e) => {
                               setMessage(e.target.value);
                           }
                       }/>
                />
                <button style={{
                    background: 'transparent',
                    borderBottomLeftRadius: '10px',
                    borderBottomRightRadius: '10px',
                    color: 'white',
                    opacity: 0.8,
                    height: '35px',
                    marginTop: '5px'
                }}
                onClick={(e) => {
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

                }}>
                    Отправить
                </button>
            </div>
        </div>
    );
}

export default ChatBox;
