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


const testData = [
    {
        writer: 'user',
        message: 'Здарова'
    },
    {
        writer: 'admin',
        message: 'чо случилось'
    },
    {
        writer: 'user',
        message: 'твой сайт гавно'
    },
    {
        writer: 'admin',
        message: 'я знаю'
    },
]
const Chat = () => {
    return (
        <div style={{
            width: '300px',
            height: '400px',
            backgroundColor: '#092754',
            border: '2px solid #CFB82E',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            borderRadius: '10px',
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
                }} type="text" placeholder='Ваше имя'/>
            </div>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                {testData.map((msg, index) => {
                    return <div style={{
                        alignSelf: msg.writer === 'user' ? 'end' : 'start',
                        border: '1px solid #CFB82E',
                        color: 'white',
                        margin: '5px',
                        padding: '3px',
                        borderRadius: '10px'
                    }}>
                        <p style={{
                            textAlign: msg.writer === 'user' ? 'right' : 'left',
                            color: 'gray'
                        }}>{msg.writer}</p>
                        <p>{msg.message}</p>
                    </div>
                })}
            </div>
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                <input style={{
                    height: '25px',
                    padding: '3px'
                }} type="text" placeholder='Сообщение'/>
                <button style={{
                    background: 'transparent',
                    borderBottomLeftRadius: '10px',
                    borderBottomRightRadius: '10px',
                    color: 'white',
                    opacity: 0.8,
                    height: '35px',
                    marginTop: '5px'
                }}>отправить
                </button>
            </div>
        </div>
    );
};


const SupportChat = () => {
    const [name, setName] = useState('');
    const [message, setMessage] = useState('');
    const [answer, setAnswer] = useState('Ответ от сервера');

    showAnswer = setAnswer;

    return (
        <div>
            <form action="">
                <input type="text" placeholder='Ваше имя' value={name}
                       onChange={
                           (e) => {
                               setName(e.target.value);
                           }
                       }/>
                <br/>
                <input type="text" placeholder='Сообщение' value={message}
                       onChange={
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
            <textarea name="text" id="" cols="30" rows="10" value={answer}
                      readonly={true}></textarea>
            <Chat/>
        </div>
    );
};

export default SupportChat;