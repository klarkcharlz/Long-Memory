import React from "react";
import {Link, useNavigate} from "react-router-dom";
import classes from "./Header.module.css";

const logout = () => {
    console.log('logout')
}

const Header = ({token, setToken}) => {
    const navigate = useNavigate();
    return (
        <div>

            <div className={classes.header}>
                <div>
                    <Link to='/main'>
                        <button>О проекте</button>
                    </Link>
                </div>

                {!token ?
                    <div>
                        <Link to='/registration'>
                            <button onClick={() => {
                                setToken(true);
                            }}>Регистрация
                            </button>
                        </Link>
                        <Link to='/authorization'>
                            <button onClick={() => {
                                setToken(true);
                            }}>Авторизация
                            </button>
                        </Link>

                    </div> : <div>
                        <button onClick={() => {
                            logout();
                            navigate("/main");
                            setToken(false);
                        }
                        }>Выход
                        </button>
                    </div>
                }
            </div>

            <h1>Long Memory</h1>
        </div>
    )
}

export default Header;
