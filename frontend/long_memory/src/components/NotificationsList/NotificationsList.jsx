import React, {useEffect, useState} from "react";
import classes from "./NotificationsList.module.css";
import useUserContext from "../../hooks/useUserContext";
import {getUserNotifications} from "../../functions/api";
import {formatDate} from "../../functions/utils";


const testData =
    {
        id: 1,
        title: 'Programming',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In facilisis pretium mauris vel mattis. Phasellus ut augue auctor, lacinia magna a, efficitur nibh. Donec eget euismod mi, eu ullamcorper urna. Donec rhoncus sit amet lacus nec vehicula. Nullam non rutrum mauris. Ut convallis tortor sed est imperdiet, sed tristique risus dignissim. Praesent blandit rhoncus magna, a vulputate massa sagittis sit amet. Proin vitae porttitor turpis. Nam in molestie erat.',
        created_at: new Date().toString(),
        next_notifications: new Date().toString(),
    }

const Notification = ({notification}) => {
    const {title, description, created_at, next_notifications} = notification;
    return (
        <div className={classes.container}>
            <div className={classes.notification_container}>
                <p>{title}</p>
                <p>{description}</p>
                <p>создано: {formatDate(created_at)}</p>
                <p>напоминание: {formatDate(next_notifications)}</p>
            </div>
            <div className={classes.button}>
                <button>Повторил</button>
                <button>Больше не показывать</button>
            </div>
        </div>
    )
}

const NotificationList = () => {
    const [notifications, setNotifications] = useState([]);
    const {token} = useUserContext();

    useEffect(() => {
        if (token) {
            getUserNotifications(token, setNotifications)
        }
    }, [token]);

    if (notifications.length !== 0) {
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
    return <h2>У вас пока не создано ни одного напоминания.</h2>

}

export default NotificationList;
