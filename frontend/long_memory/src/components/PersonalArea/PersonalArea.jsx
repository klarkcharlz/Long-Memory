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
                    <label className={classes.inner_container}>
                        <span>Telegram</span>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="id"/>
                        </div>
                    </label>
                    <label className={classes.inner_container}>
                        <span>Vkontakte</span>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="id"/>
                        </div>
                    </label>
                    <label className={classes.inner_container}>
                        <span>Email</span>
                        <div>
                            <input type="checkbox"/>
                            <input className={classes.input_area} type="text" placeholder="email"/>
                        </div>
                    </label>
                </div>

                <div className={classes.container}>

                    <h3>Дополнительные данные</h3>

                    <div className={classes.name_container}>
                        <div>
                            <p>Ваше имя</p>
                            <input className={classes.input_area} type="text"/>
                        </div>
                        <div>
                            <p>Аватар</p>
                            <div className={classes.file_upload}>
                                <label>
                                    <input type="file" name="file" id="uploade-file"/>
                                    <span>Выберите файл</span>
                                </label>
                            </div>
                        </div>
                        <button className={classes.button}>Сохранить</button>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default PersonalArea;
