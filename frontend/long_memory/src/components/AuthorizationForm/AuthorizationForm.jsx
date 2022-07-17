import React, { useState } from "react";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userAuthorization} from "../../functions/api"


const authorization = (username, password, navigate, setToken) => {
    console.log('Авторизация');
    console.log(username);
    console.log(password);
    userAuthorization(username, password, (token) => {setToken(token)}, navigate);
}


const AuthorizationForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const {setToken} = useUserContext();
    return (
        <div>
            <form>

                <label> Username
                    <input type="text"
                           name="username"
                           value={username}
                           onChange={(e) => {
                               setUsername(e.target.value)
                           }}
                    />
                </label>

                <br/>

                <label> Password
                    <input type="password"
                        name="password"
                        value={password}
                        onChange={(e) => {
                            setPassword(e.target.value);
                        }}
                    />
                </label>

                <br/>

                <button type="button" onClick={() => {
                    authorization(username, password, navigate, setToken);
                }}>Регистрация
                </button>

            </form>
        </div>
    )
}

export default AuthorizationForm;
