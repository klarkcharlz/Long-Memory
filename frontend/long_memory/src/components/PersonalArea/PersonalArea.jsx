import React, {useEffect, useState} from "react";
import classes from "./PersonalArea.module.css";
import {Tooltip} from "@mui/material";
import HelpOutlineIcon from '@mui/icons-material/HelpOutline';
import {blue} from '@mui/material/colors';
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";
import {getUserData, updateUser} from "../../functions/api"
import Avatar from 'react-avatar-edit'
import AvatarModal from "../AvatarModal/AvatarModal";
import Loader from "../Loader/Loader";

const Helper = () => {
    return (
        <div className={classes.helper}>
            <span>
                <a href="https://t.me/Longmemory_bot" rel="noreferrer" target="_blank">
                    <svg className={classes.logo_telegram}></svg>
                </a>
            </span>
            {/*<h2>Телеграм</h2>*/}
            <h3>Чтобы получить свой id в телеграм, напишите
                <a href="https://t.me/Longmemory_bot" rel="noreferrer" target="_blank"> нашему боту</a>
                , введите команду /start или нажмите кнопку старт и получите свой id в телеграм, после чего можете
                сохранить его здесь.
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

const AvatarEditor = ({userData, setUserData}) => {

    const [preview, setPreview] = useState('')

    return (
        <div className={classes.avatar_modal}>
            <div className={classes.empty_area}>
                <Avatar
                    width={300}
                    height={300}
                    imageWidth={300}
                    onCrop={(value) => {
                        setPreview(value)
                    }}
                    onClose={() => {
                        setPreview(null)
                    }}
                />
            </div>
            <button onClick={(e) => {
                e.preventDefault()
                setUserData({
                    ...userData,
                    avatar: preview
                })
            }}
                    className={classes.button_avatar}>Сохранить
            </button>

        </div>
    )
}

const validateUserInfo = (userData) => {
    let error = [];
    let validate;

    if(userData.vk_reminders && !userData.vk_id) error.push("Вк id не может быть пустым.<br/>");
    if(userData.telegram_reminders && !userData.telegram_id) error.push("Телеграм id не может быть пустым.<br/>");
    if(userData.email_reminders && !userData.email) error.push("Email не может быть пустым.");

    if(error.length >= 1) validate = false;
    else validate = true;

    return [validate, error];
}

const updateUser_ = (setStatus, token, userData) => {
    console.log('New user data > ', userData)
    const [valid, error] = validateUserInfo(userData);
    if(valid) updateUser(token, userData, setStatus);
    else setStatus(error.join('\n'));
}

const getUserInfo = (setStatus, token, setUserData, endLoading) => {
    getUserData(setStatus, token, setUserData, endLoading)
}

const defaultAvatar = "https://mir-avatarok.3dn.ru/_si/0/43720430.jpg";

const PersonalArea = () => {
    const {token} = useUserContext();
    const setStatus = useStatusModalHook();
    const [userData, setUserData] = useState({});
    const [activeAvatarModal, setAcitveAvatarModal] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    const endLoading = () => {
        setIsLoading(false);
    }

    useEffect(() => {
        if (token) {
            setIsLoading(true);
            // getUserInfo(setStatus, token, setUserData, endLoading)
            setTimeout(() => {
                getUserInfo(setStatus, token, setUserData, endLoading);
            }, 3000)
        }
    }, [token]);

    if(isLoading) return <div style={{display: 'flex', justifyContent: 'center', marginTop: 150}}><Loader/></div>

    return (
        <div className={classes.main}>

            <div className={classes.avatar} onClick={(event) => {
                event.preventDefault()
                setAcitveAvatarModal(true)
            }}>
                <img src={userData.avatar ? userData.avatar : defaultAvatar} alt="Аватар"/>
            </div>

            <AvatarModal open={activeAvatarModal}
                         setOpen={setAcitveAvatarModal}
                         children={<AvatarEditor
                             setUserData={setUserData}
                             userData={userData}
                         />}/>

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
                            <p>Username</p>
                            <input
                                value={userData.username}
                                className={classes.input_area}
                                type="text"
                                onChange={(e) => {
                                    e.preventDefault();
                                    setUserData({
                                        ...userData,
                                        username: e.target.value
                                    });
                                }}/>
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
