import React, {useState} from "react";
import classes from "./NotificationsList.module.css";


import {getContent} from '../../functions/api'


const testData =
    {
        id: 1,
        title: 'Programming',
        description: 'Learn Programming',
        date: new Date().toString()
    }


const Notification = ({notification}) => {
    const {title, description, date} = notification;
    return (
        <div className={classes.container}>
            <p>{title}</p>
            <p>{description}</p>
            <p>{date}</p>
            <div className={classes.button}>
                <button>Повторил</button>
                <button>Больше не показывать</button>
            </div>
            <p>{date}</p>
        </div>
    )
}


const NotificationList = () => {
    const [notifications, setNotifications] = useState([testData]);
    console.log(notifications);
    return (
        <div>
            <h2>Ваши напоминания</h2>
            {notifications.map((notification) =>
                <Notification notification={notification}
                              key={notification.id}
                />)
            }
        </div>
    )
}

export default NotificationList;
