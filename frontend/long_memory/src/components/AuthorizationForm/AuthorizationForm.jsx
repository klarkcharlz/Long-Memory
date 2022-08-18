import React, { useState } from "react";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userAuthorization} from "../../functions/api"
import classes from "./AuthorizationForm.module.css";
import useStatusModalHook from "../../hooks/useStatusModalHook";

const validateUserInfo = (username, password) => {
    let error = [];
    let validate;

    if(!username) error.push("Введите логин.<br/>");
    if(!password) error.push("Введите пароль.<br/>");

    if(error.length >= 1) validate = false;
    else validate = true;

    return [validate, error];
}


const authorization = (username, password, navigate, setToken, setNotifications, setStatus) => {
    const [valid, error] = validateUserInfo(username, password);
    if(valid) userAuthorization(username, password, (token) => {setToken(token)}, navigate, setStatus);
    else setStatus(error.join('\n'));
}

const AuthorizationForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const {setToken, setNotifications} = useUserContext();
    const setStatus = useStatusModalHook();
    return (
        <div>
            <form className={classes.card_form}>

                <label className={classes.title_area}> Username
                    <input
                           className={classes.title_notification}
                           type="text"
                           name="username"
                           value={username}
                           onChange={(e) => {
                               setUsername(e.target.value)
                           }}
                    />
                </label>

                <br/>

                <label className={classes.title_area}> Password
                    <input
                        className={classes.title_notification}
                        type="password"
                        name="password"
                        value={password}
                        onChange={(e) => {
                            setPassword(e.target.value);
                        }}
                    />
                </label>

                <br/>

                <button className={classes.button} type="button" onClick={() => {
                    authorization(username, password, navigate, setToken, setNotifications, setStatus);
                }}>ВОЙТИ
                </button>

            </form>
        </div>
    )
}

export default AuthorizationForm;
