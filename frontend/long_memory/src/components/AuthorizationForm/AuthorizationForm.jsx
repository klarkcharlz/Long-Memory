import React, { useState } from "react";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userAuthorization} from "../../functions/api"
import classes from "./AuthorizationForm.module.css";


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
                    authorization(username, password, navigate, setToken);
                }}>LOGIN
                </button>

            </form>
        </div>
    )
}

export default AuthorizationForm;
