import React from "react";
import classes from "./PersonalArea.module.css";


const PersonalArea = () => {
    return (
        <div className={classes.main}>

            <div className={classes.avatar}>
                <img src="https://mir-avatarok.3dn.ru/_si/0/43720430.jpg" alt="Аватар"/>
            </div>

            <div className={classes.notification_settings}>

                <h3>Настройка уведомлений</h3>
                <br/>
                <div className={classes.container}>

                    <label className={classes.inner_container}>
                        <div>
                            <input type="checkbox"/>
                            <span>Telegram</span>
                        </div>
                        <input className={classes.input_area} type="text" placeholder="id"/>
                    </label>
                    <label className={classes.inner_container}>
                        <div>
                            <input type="checkbox"/>
                            <span>Vkontakte</span>
                        </div>
                        <input className={classes.input_area} type="text" placeholder="id"/>
                    </label>
                    <label className={classes.inner_container}>
                        <div>
                            <input type="checkbox"/>
                            <span>Email</span>
                        </div>
                        <input className={classes.input_area} type="text" placeholder="email"/>
                    </label>

                    <h4>Дополнительные данные</h4>

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
