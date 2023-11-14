import React, {useState, useRef, useEffect} from 'react';
import Message from '../Message/Message';
import {v4 as uuid} from 'uuid';
import styles from './ChatBox.module.css';
import {URL, WS_PORT, WS} from '../../functions/api_constants';

const name = 'client';

const wsConnect = () => {
    const client_id = uuid();
    const WS_URL = `${WS}://${URL}:${WS_PORT}/ws/${name}/${client_id}`;
    const ws = new WebSocket(WS_URL);
    return [client_id, ws]
}

let [client_id, ws] = wsConnect();


const sendMessage = (data) => {
    ws.send(JSON.stringify(data));
}

function ChatBox() {
    const [name, setName] = useState('');
    const [message, setMessage] = useState('');
    const [chatData, setChatData] = useState([]);

    const scrollRef = useRef(null);

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            validateMessage();
        }
    };

    const validateMessage = () => {
        if (name && message) {
            const data = {
                client_id,
                name,
                message
            }
            setChatData([...chatData, {
                writer: 'user',
                name: name,
                text: message
            }])
            sendMessage(data);
            setMessage('');
        } else {
            console.log('Empty data!')
        }
    };


    ws.onmessage = (event) => {
        const receiveData = event.data;
        setChatData([...chatData, {
            writer: 'admin',
            text: receiveData,
            name: 'admin'
        }])
    };

    useEffect(() => {
        scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }, [chatData]);

    return (
        <div className={styles.invisibleScroll} style={{
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
            </div>
            <div className={styles.invisibleScroll} style={{
                display: 'flex',
                flexDirection: 'column',
                maxHeight: '300px',
            }} ref={scrollRef}>
                {chatData.map((msg, index) => {
                    return <Message writer={msg.writer} text={msg.text} name={msg.name}
                                    key={index}/>
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
                       onKeyUp={handleKeyPress}
                       onChange={
                           (e) => {
                               setMessage(e.target.value);
                           }
                       }/>
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
                            validateMessage();
                        }}>
                    Отправить
                </button>
            </div>
        </div>
    );
}

export default ChatBox;