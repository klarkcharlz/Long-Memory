import React from "react";
import classes from "./PersonalArea.module.css";
import {Tooltip} from "@mui/material";
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import {blue} from '@mui/material/colors';


const Helper = () => {
    return (
        <div>
            <h2>Телеграм</h2>
            <h3>Чтобы получить свой id в телеграм,
                напишите <a href="https://t.me/long_memory_bot" target="_blank">нашему боту</a>,
                введите команду /start или нажмите кнопку старт
                и получите свой id в телеграм, после чего можете сохранить его здесь.</h3>
            <h2>ВК</h2>
            <h3>Чтобы получать сообщения в ВК вступите в <a href="https://vk.com/public214673853" target="_blank">нашу группу</a> и напишите любое сообщение в личное сообщение группы.</h3>
        </div>
    )
}


const PersonalArea = () => {
    return (
        <div className={classes.main}>

            <div className={classes.avatar}>
                <img src="https://mir-avatarok.3dn.ru/_si/0/43720430.jpg" alt="Аватар"/>
            </div>

            <div className={classes.notification_settings}>

                <h3>Настройка уведомлений &nbsp;<Tooltip title={
                    <Helper/>
                }>
                    <HelpOutlineIcon sx={{color: blue[100]}}/>
                </Tooltip></h3>


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
