import React, {useState} from "react";
import classes from "./RegistrationForm.module.css";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userRegistration} from "../../functions/api"
import useStatusModalHook from "../../hooks/useStatusModalHook";

const validateUserInfo = (username, email, password1, password2) => {
    let error = [];
    let validate;

    if (!username) error.push("Введите логин.<br/>");
    if (!email) error.push("Заполните адрес электронной почты.<br/>");
    if (!password1) error.push("Введите пароль.<br/>");
    if (!password2) error.push("Подтвердите пароль.<br/>");

    if (error.length >= 1) validate = false;
    else validate = true;

    return [validate, error];
}


const registration = (
    username, email, password1,
    password2, navigate,
    setStatus, offDisabledButton, onDisabledButton) => {
    // console.log('регистрация');
    const [valid, error] = validateUserInfo(username, email, password1, password2);
    if (valid) {
        if (password1 === password2) {
            // console.log("Регистрация")
            userRegistration(password1, username, email, navigate, setStatus, offDisabledButton, onDisabledButton)
        } else {
            setStatus('Пароли не совпадают.')
        }
    } else setStatus(error.join('\n'));
}


const RegistrationForm = () => {
    const [disableButton, setDisableButton] = useState(false);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const navigate = useNavigate();
    const {setToken} = useUserContext();
    const setStatus = useStatusModalHook();

    const offDisabledButton = () => {
        setDisableButton(false);
    }

    const onDisabledButton = () => {
        setDisableButton(true);
    }

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

                <button
                    disabled={disableButton}
                    className={classes.button}
                    onClick={(e) => {
                        e.preventDefault();
                        registration(username, email, password1,
                            password2, navigate,
                            setStatus, offDisabledButton, onDisabledButton);
                    }}>РЕГИСТРАЦИЯ
                </button>

            </form>

        </div>
    )
}

export default RegistrationForm;
