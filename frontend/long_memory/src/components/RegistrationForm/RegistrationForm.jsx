import React, {useState} from "react";
import classes from "./RegistrationForm.module.css";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userRegistration} from "../../functions/api"
import useStatusModalHook from "../../hooks/useStatusModalHook";



const registration = (username, email, password1, password2, navigate, setToken, setStatus) => {
    if (password1 === password2) {
        console.log("Регистрация")
        userRegistration(password1, username, email, (token) => {
            setToken(token)
        }, navigate, setStatus)
    }
    else{
        setStatus('Пароли не совпадают.')
    }
}


const RegistrationForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const navigate = useNavigate();
    const {setToken} = useUserContext();
    const setStatus = useStatusModalHook();
    return (
        <div>

            <form className={classes.card_form}>

                <label className={classes.title_area}>Username
                    <input type="text"
                           name="username"
                           value={username}
                           onChange={(e) => {
                               setUsername(e.target.value)
                           }}
                    />
                </label>

                <br/>

                <label> Email
                    <input type="text"
                           name="email"
                           value={email}
                           onChange={(e) => {
                               setEmail(e.target.value);
                           }}
                    />
                </label>

                <br/>

                <label>Password
                    <input type="password"
                           name="password1"
                           value={password1}
                           onChange={(e) => {
                               setPassword1(e.target.value);
                           }}
                    />
                </label>

                <br/>

                <label>Password
                    <input type="password"
                           name="password2"
                           value={password2}
                           onChange={(e) => {
                               setPassword2(e.target.value);
                           }}
                    />
                </label>

                <br/>

                <button className={classes.button} onClick={(e) => {
                    e.preventDefault();
                    registration(username, email, password1, password2, navigate, setToken, setStatus);
                }}>РЕГИСТРАЦИЯ
                </button>

            </form>

        </div>
    )
}

export default RegistrationForm;
