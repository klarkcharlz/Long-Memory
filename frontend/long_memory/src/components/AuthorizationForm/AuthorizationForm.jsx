import React, { useState } from "react";


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
                    authorization(username, password);
                }}>Регистрация
                </button>

            </form>
        </div>
    )
}

export default AuthorizationForm;
