import {Link} from "react-router-dom";
import React from "react";
import classes from "./UserMenu.module.css";
import useUserContext from "../../hooks/useUserContext"

const UserMenu = () => {
    const {token} = useUserContext();
    if(!token){
        return (
            <nav className={classes.container}></nav>
        )
    }
    return (
        <nav className={classes.container}>
            <Link className={classes.link} to='/create_notification'><button className={classes.button}>Создать<br/>карточку</button></Link>
            <Link className={classes.link} to='/notifications_list'><button className={classes.button}>Показать<br/>карточки</button></Link>
            <Link className={classes.link} to='/pa'><button className={classes.button}>Личный<br/>кабинет</button></Link>
        </nav>
    )
}

export default UserMenu;
