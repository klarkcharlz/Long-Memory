import React, {createContext, useState} from 'react';


const UserContext = createContext({});

const UserProvider = ({children}) => {
    const [token, setToken] = useState("");
    const [modalStatus, setModalStatus] = useState(false);
    const [statusText, setStatusText] = useState("");

    return (
        <UserContext.Provider
        value={{token, setToken, modalStatus, setModalStatus, statusText, setStatusText}}>
            {children}
        </UserContext.Provider>
    )
}


export {UserProvider, UserContext};
