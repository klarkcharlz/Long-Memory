import React from 'react';
import SupportAgentIcon from '@mui/icons-material/SupportAgent';


function ChatButton({ toggleChat }) {
    return (
        <button onClick={toggleChat} style={{
            position: 'fixed',
            bottom: '20px',
            right: '20px',
            borderRadius: '50%',
            fontSize: '24px'
        }}><SupportAgentIcon/></button>
    );
}

export default ChatButton;