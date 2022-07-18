import React, {createContext, useState} from 'react';


const UserContext = createContext({});

const UserProvider = ({children}) => {
    const [token, setToken] = useState("");
    const [notifications, setNotifications] = useState([]);
    return (
        <UserContext.Provider
        value={{token, setToken}}>
            {children}
        </UserContext.Provider>
    )
}


export {UserProvider, UserContext};
