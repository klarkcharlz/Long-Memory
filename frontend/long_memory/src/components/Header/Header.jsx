import React from "react";
import {Link, useNavigate} from "react-router-dom";
import classes from "./Header.module.css";
import useUserContext from "../../hooks/useUserContext";
import {set_token_to_storage} from "../../functions/tokenStorage"

const logout = (setToken, navigate) => {
    navigate("/main");
    setToken("");
    set_token_to_storage("");
}

const Header = () => {
    const navigate = useNavigate();
    const {token, setToken} = useUserContext();
    return (
        <div className={classes.container}>
            <div className={classes.header}>
                <div className={classes.logo_title}>
                    <Link to='/main'>
                        <button className={classes.button_logo}>Главная</button>
                    </Link>
                    <Link to='/materials'>
                        <button className={classes.button_logo_materials}>Доп.<br/>материалы</button>
                    </Link>
                    <div className={classes.title}>
                        <h1>Long Memory</h1>
                    </div>
                </div>

                {!token ?
                    <div className={classes.user_menu}>
                        <a className={classes.button} href='https://oauth.vk.com/authorize?client_id=51403117&display=page&redirect_uri=http://localhost:3000/vk_auth&scope=friends,email,offline&response_type=token&v=5.131'>
                        <img className={classes.vk_logo} />
                        </a>
                        <Link to='/registration'>
                            <button className={classes.button}>Регистрация</button>
                        </Link>
                        <Link to='/authorization'>
                            <button className={classes.button}>Войти</button>
                        </Link>

                    </div>
                    :
                    <div>
                        <button className={classes.button} onClick={() => {
                            logout(setToken, navigate);
                        }
                        }>Выход
                        </button>
                    </div>}

            </div>
        </div>
    )
}

export default Header;
