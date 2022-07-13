import React from "react";
import {Link} from "react-router-dom";
import classes from "./Header.module.css";

const Header = () => {
    return (
        <div>

            <div className={classes.header}>
                <div>
                    <Link to='/main'>
                        <button>О проекте</button>
                    </Link>
                </div>

                <div>
                    <Link to='/main'>
                        <button>Регистрация</button>
                    </Link>
                    <Link to='/main'>
                        <button>Авторизация</button>
                    </Link>
                </div>
        </div>

    <h1>Long Memory</h1>
</div>
)
}

export default Header;
