import React, {createContext, useState} from 'react';


const UserContext = createContext({});

const UserProvider = ({children}) => {
    const [token, setToken] = useState("");
    const [modalStatus, setModalStatus] = useState(false);
    const [statusText, setStatusText] = useState("");
    const [modalContent, setModalContent] = useState(<></>);

    return (
        <UserContext.Provider
            value={{
                token, setToken, modalStatus,
                setModalStatus, statusText, setStatusText,
                modalContent, setModalContent
            }}>
            {children}
        </UserContext.Provider>
    )
}


export {UserProvider, UserContext};
