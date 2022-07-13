import {Link} from "react-router-dom";
import React from "react";

import classes from "./Menu.module.css";

const Menu = () => {
    return (
        <nav>
            <ul>
                <li><Link to='/create_notification'><button className={classes.button}>Создать напоминание.</button></Link></li>
                <li><Link to='/notifications_list'><button className={classes.button}>Активные напоминания.</button></Link></li>
            </ul>
        </nav>
    )
}

export default Menu;
