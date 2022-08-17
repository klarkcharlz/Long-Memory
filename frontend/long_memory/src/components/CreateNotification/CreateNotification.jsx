import React, {useState} from "react";
import classes from "./CreateNotification.module.css";
import {createNotification, updateUser} from "../../functions/api"
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";

const validateUserInfo = (notification) => {
    let error = [];
    let validate;

    if(!notification.title) error.push("Тема не может быть пустой.<br/>");
    if(!notification.description) error.push("Описание не может быть пустым.<br/>");

    if(error.length >= 1) validate = false;
    else validate = true;

    return [validate, error];
}

const createNotification_ = (title, description, token, clearForm, setStatus) => {
    const notification = {
        title,
        description
    }
    const [valid, error] = validateUserInfo(notification);
    if(valid) createNotification(notification, token, setStatus, clearForm);
    else setStatus(error.join('\n'));
}


const CreateNotification = () => {
    const [title, setTitle] = useState('React hooks');
    const [description, setDescription] = useState('useState');
    const {token} = useUserContext();
    const clearForm = () =>{
        setTitle("");
        setDescription("");
    }
    const setStatus = useStatusModalHook();
    return (
        <div>
            <form className={classes.card_form}>
                <label className={classes.title_area}>Тема(ы)
                    <input
                        className={classes.title_notification}
                        type="text"
                        name="title"
                        value={title}
                        onChange={(e) => {
                            setTitle(e.target.value)
                        }}
                    />
                </label>
                <br/>
                <label className={classes.area_form}>Описание
                    <textarea className={classes.theme_notification}
                        name="description"
                        value={description}
                        onChange={(e) => {
                            setDescription(e.target.value);
                        }}
                    />
                </label>
                <br/>
                <button className={classes.button} type="button" onClick={() => {
                    createNotification_(title, description, token, clearForm, setStatus);
                }}>СОЗДАТЬ
                </button>
            </form>
        </div>
    )
}

export default CreateNotification;
