import React, {useState} from "react";
import classes from "./CreateNotification.module.css";


const createNotification = (title, description) => {
    console.log('Создано');
    console.log(title);
    console.log(description);
}


const CreateNotification = () => {
    const [title, setTitle] = useState('React hooks');
    const [description, setDescription] = useState('useState');
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
                    createNotification(title, description);
                }}>CREATE
                </button>
            </form>
        </div>
    )
}

// export default CreateNotification;
export default CreateNotification;
