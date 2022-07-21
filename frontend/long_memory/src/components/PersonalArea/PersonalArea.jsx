import React from "react";
import classes from "./PersonalArea.module.css";


const PersonalArea = () => {
    return (
        <div>

            <div className={classes.avatar}>
                <img src="https://mir-avatarok.3dn.ru/_si/0/43720430.jpg" alt="Аватар"/>
            </div>

            <div className={classes.notification_settings}>

                <h3>Настройка уведомлений</h3>

                <div className={classes.container}>
                    <div className={classes.inner_container}>
                        <p>Telegram</p>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="id/email"/>
                        </div>
                    </div>
                    <div className={classes.inner_container}>
                        <p>Vkontakte</p>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="id/email"/>
                        </div>
                    </div>
                    <div className={classes.inner_container}>
                        <p>Email</p>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="email"/>
                        </div>
                    </div>
                </div>

                <div className={classes.container}>

                    <h3>Дополнительные данные</h3>

                    <div className={classes.container}>
                        <div>
                            <p>Ваше имя</p>
                            <input type="text"/>
                        </div>
                        <div>
                            <p>Аватар</p>
                            <input type="file"/>
                        </div>
                    </div>
                    <button className={classes.button}>Сохранить</button>
                </div>
            </div>
        </div>
    )
}

export default PersonalArea;
