import React, {useState} from "react";
import classes from "./CreateNotification.module.css";
import {createNotification} from "../../functions/api"
import useUserContext from "../../hooks/useUserContext";

const createNotification_ = (title, description, token) => {
    console.log('Создано');
    const notification = {
        title,
        description
    }
    // createNotification(notification, token)
}


const CreateNotification = () => {
    const [title, setTitle] = useState('React hooks');
    const [description, setDescription] = useState('useState');
    const {token} = useUserContext();
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
                    createNotification_(title, description, token);
                }}>CREATE
                </button>
            </form>
        </div>
    )
}

export default CreateNotification;
