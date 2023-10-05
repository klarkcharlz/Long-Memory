import React from 'react';

function Message({text, writer}) {
    return (
        <div style={{
            alignSelf: writer === 'user' ? 'end' : 'start',
            border: '1px solid #CFB82E',
            color: 'white',
            margin: '5px',
            padding: '3px',
            borderRadius: '10px'
        }}>
            <p style={{
                textAlign: writer === 'user' ? 'right' : 'left',
                color: 'gray'
            }}>{writer}</p>
            <p>{text}</p>
        </div>
    );
}

export default Message;
