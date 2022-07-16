import React from "react";
import {Link} from "react-router-dom";
import classes from "./Header.module.css";

const logout = () => {
    console.log('logout')
}

const Header = () => {
    return (
        <div>
            <div className={classes.header}>
                <div>
                    <Link to='/main'>
                        <button className={classes.button_logo}>Main</button>
                    </Link>
                </div>

                <div className={classes.user_menu}>
                    <Link to='/registration'>
                        <button className={classes.button}>Login</button>
                    </Link>
                    <Link to='/authorization'>
                        <button className={classes.button}>Sign up</button>
                    </Link>
                </div>

            </div>

            <div className={classes.title}>
                <h1>Long Memory</h1>
            </div>

        </div>
    )
}

export default Header;
