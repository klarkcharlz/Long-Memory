import React, {useState} from "react";


const registration = (username, email, password1, password2) => {
    console.log('Регистрация');
    console.log(username);
    console.log(email);
    console.log(password1);
    console.log(password2);
    console.log(password1 == password2);
    // запрос на бэк(username, email, password)
}


const RegistrationForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
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

                <button type="button" onClick={() => {
                    registration(username, email, password1, password2);
                }}>Регистрация
                </button>

            </form>
        </div>
    )
}

export default RegistrationForm;
