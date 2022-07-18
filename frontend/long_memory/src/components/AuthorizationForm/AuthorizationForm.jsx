import React, { useState } from "react";
import classes from "./AuthorizationForm.module.css";


const authorization = (username, password) => {
    console.log('Авторизация');
    console.log(username);
    console.log(password);
}


const AuthorizationForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
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
                    authorization(username, password);
                }}>LOGIN
                </button>

            </form>
        </div>
    )
}

export default AuthorizationForm;
