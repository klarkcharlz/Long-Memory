import React from "react";
import {Link, useNavigate} from "react-router-dom";
import classes from "./Header.module.css";
import useUserContext from "../../hooks/useUserContext";
import {set_token_to_storage} from "../../functions/tokenStorage"

const logout = (setToken, navigate) => {
    console.log('logout');
    navigate("/main");
    setToken("");
    set_token_to_storage("");
}

const Header = () => {
    const navigate = useNavigate();
    const {token, setToken} = useUserContext();
    return (
        <div>
            <div className={classes.header}>
                <div>
                    <Link to='/main'>
                        <button className={classes.button_logo}>Main</button>
                    </Link>
                </div>

                {!token ?
                    <div className={classes.user_menu}>
                        <Link to='/registration'>
                            <button className={classes.button}>Login</button>
                        </Link>
                        <Link to='/authorization'>
                            <button className={classes.button}>Sign up</button>
                        </Link>
                    </div>
                    :
                    <div>
                        <button onClick={() => {
                            logout(setToken, navigate);
                        }
                        }>Выход
                        </button>
                    </div>}

            </div>

            <div className={classes.title}>
                <h1>Long Memory</h1>
            </div>

        </div>
    )
}

export default Header;
