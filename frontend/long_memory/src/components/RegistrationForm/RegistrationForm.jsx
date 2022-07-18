import React, {useState} from "react";
import classes from "./RegistrationForm.module.css";
import {useNavigate} from "react-router-dom";
import useUserContext from "../../hooks/useUserContext";
import {userRegistration} from "../../functions/api"


const registration = (username, email, password1, password2, navigate, setToken) => {
    console.log('Регистрация');
    console.log(username);
    console.log(email);
    console.log(password1);
    console.log(password2);
    console.log(password1 == password2);
    // userRegistration(password, username, email, (token) => {setToken(token)}, navigate)
}


const RegistrationForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const navigate = useNavigate();
    const {setToken} = useUserContext();
    return (
        <div>

            <form className={classes.card_form}>

                <label className={classes.title_area}> Username
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

                <label> Password
                    <input type="password"
                           name="password1"
                           value={password1}
                           onChange={(e) => {
                               setPassword1(e.target.value);
                           }}
                    />
                </label>

                <br/>

                <label> Password
                    <input type="password"
                           name="password2"
                           value={password2}
                           onChange={(e) => {
                               setPassword2(e.target.value);
                           }}
                    />
                </label>

                <br/>

                <button className={classes.button} onClick={() => {
                    registration(username, email, password1, password2, navigate, setToken);
                }}>REGISTRATION
                </button>

            </form>

        </div>
    )
}

export default RegistrationForm;
