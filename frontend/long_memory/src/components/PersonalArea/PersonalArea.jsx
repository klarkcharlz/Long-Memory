import React, {useEffect, useState} from "react";
import classes from "./PersonalArea.module.css";
import {Tooltip} from "@mui/material";
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import {blue} from '@mui/material/colors';
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";
import {getUserData, updateUser} from "../../functions/api"

const Helper = () => {
    return (
        <div className={classes.helper}>
            <span>
                <a href="https://t.me/long_memory_bot" rel="noreferrer" target="_blank">
                    <svg className={classes.logo_telegram}></svg>
                </a>
            </span>
            {/*<h2>Телеграм</h2>*/}
            <h3>Чтобы получить свой id в телеграм, напишите
                <a href="https://t.me/long_memory_bot" rel="noreferrer" target="_blank"> нашему боту</a>
                , введите команду /start или нажмите кнопку старт и получите свой id в телеграм, после чего можете сохранить его здесь.
            </h3>
            <br/>
            <span>
                <a href="https://vk.com/public214673853" rel="noreferrer" target="_blank">
                    <svg className={classes.logo_vk}></svg>
                </a>
                {/*<h2>ВК</h2>*/}
            </span>
            <h3>Чтобы получать сообщения в ВК
                вступите в <a href="https://vk.com/public214673853" rel="noreferrer"
                   target="_blank"> нашу группу
                </a> и напишите любое сообщение в личное сообщение группы.
            </h3>
        </div>
    )
}

const updateUser_ = (setStatus, token, userData) => {
    console.log('New user data > ', userData)
    updateUser(token, userData, setStatus);
}

const getUserInfo = (setStatus, token, setUserData) => {
    getUserData(setStatus, token, setUserData)
}

const defaultAvatar = "https://mir-avatarok.3dn.ru/_si/0/43720430.jpg";

const PersonalArea = () => {
    /*avatar: null
    email: "admin@admin.ru"
    email_reminders: false
    first_name: "Николай"
    telegram_id: ""
    telegram_reminders: false
    vk_id: "12345"
    vk_reminders: false*/
    const {token} = useUserContext();
    const setStatus = useStatusModalHook();
    const [userData, setUserData] = useState({});

    useEffect(() => {
        if (token) {
            getUserInfo(setStatus, token, setUserData)
        }
    }, [token]);

    return (
        <div className={classes.main}>

            <div className={classes.avatar}>
                <img src={userData.avatar ? userData.avatar: defaultAvatar} alt="Аватар"/>
            </div>

            <div className={classes.notification_settings}>

                <h3>Настройка уведомлений &nbsp;<Tooltip title={
                    <Helper/>
                }>
                    <HelpOutlineIcon sx={{color: blue[100]}}/>
                </Tooltip></h3>
                <br/>
                <div className={classes.container}>

                    <label className={classes.inner_container}>
                        <div>
                            <input
                                checked={userData.telegram_reminders}
                                type="checkbox"
                                onChange={(e) => {
                                    setUserData({
                                        ...userData,
                                        telegram_reminders: !userData.telegram_reminders
                                    });
                                }}/>
                            <span>Telegram</span>
                        </div>
                        <input
                            value={userData.telegram_id}
                            className={classes.input_area}
                            type="text"
                            placeholder="id"
                            onChange={(e) => {
                                e.preventDefault();
                                setUserData({
                                    ...userData,
                                    telegram_id: e.target.value
                                });
                            }}/>
                    </label>
                    <label className={classes.inner_container}>
                        <div>
                            <input
                                checked={userData.vk_reminders}
                                type="checkbox"
                                onChange={(e) => {
                                    setUserData({
                                        ...userData,
                                        vk_reminders: !userData.vk_reminders
                                    });
                                }}/>
                            <span>Vkontakte</span>
                        </div>
                        <input
                            value={userData.vk_id}
                            className={classes.input_area}
                            type="text"
                            placeholder="id"
                            onChange={(e) => {
                                e.preventDefault();
                                setUserData({
                                    ...userData,
                                    vk_id: e.target.value
                                });
                            }}
                        />
                    </label>
                    <label className={classes.inner_container}>
                        <div>
                            <input
                                checked={userData.email_reminders}
                                type="checkbox"
                                onChange={(e) => {
                                    setUserData({
                                        ...userData,
                                        email_reminders: !userData.email_reminders
                                    });
                                }}/>
                            <span>Email</span>
                        </div>
                        <input
                            value={userData.email}
                            className={classes.input_area}
                            type="text"
                            placeholder="email"
                            onChange={(e) => {
                                e.preventDefault();
                                setUserData({
                                    ...userData,
                                    email: e.target.value
                                });
                            }}/>
                    </label>

                    <h4>Дополнительные данные</h4>

                    <div className={classes.name_container}>
                        <div>
                            <p>Ваше имя</p>
                            <input
                                value={userData.first_name}
                                className={classes.input_area}
                                type="text"
                                onChange={(e) => {
                                    e.preventDefault();
                                    setUserData({
                                        ...userData,
                                        first_name: e.target.value
                                    });
                                }}/>
                        </div>
                        <div>
                            <p>Аватар</p>
                            <div className={classes.file_upload}>
                                <label>
                                    <input
                                        type="file"
                                        name="file"
                                        id="uploade-file"
                                    />
                                    <span>Выберите файл</span>
                                </label>
                            </div>
                        </div>
                        <button className={classes.button} onClick={(e) => {
                            e.preventDefault();
                            updateUser_(setStatus, token, userData);
                        }}>Сохранить
                        </button>
                    </div>

                </div>
            </div>
        </div>
    )
}

export default PersonalArea;
