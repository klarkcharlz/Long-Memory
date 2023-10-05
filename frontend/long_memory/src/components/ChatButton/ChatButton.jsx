import React from 'react';

function ChatButton({ toggleChat }) {
    return (
        <button onClick={toggleChat} style={{
            position: 'fixed',
            bottom: '20px',
            right: '20px',
            borderRadius: '50%',
            fontSize: '24px'
        }}>☰</button>
    );
}

export default ChatButton;