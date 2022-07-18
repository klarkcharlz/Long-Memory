import React, {useState} from "react";
import classes from "./NotificationsList.module.css";


import {getContent} from '../../functions/api'


const testData =
    {
        id: 1,
        title: 'Programming',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In facilisis pretium mauris vel mattis. Phasellus ut augue auctor, lacinia magna a, efficitur nibh. Donec eget euismod mi, eu ullamcorper urna. Donec rhoncus sit amet lacus nec vehicula. Nullam non rutrum mauris. Ut convallis tortor sed est imperdiet, sed tristique risus dignissim. Praesent blandit rhoncus magna, a vulputate massa sagittis sit amet. Proin vitae porttitor turpis. Nam in molestie erat.',
        date: new Date().toString()
    }


const Notification = ({notification}) => {
    const {title, description, date} = notification;
    return (
        <div className={classes.container}>
            <div className={classes.notification_container}>
                <p>{title}</p>
                <p>{description}</p>
                <p>{date}</p>
            </div>
            <div className={classes.button}>
                <button>Повторил</button>
                <button>Больше не показывать</button>
            </div>
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
