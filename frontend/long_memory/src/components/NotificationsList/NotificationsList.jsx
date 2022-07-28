import React, {useEffect, useState} from "react";
import classes from "./NotificationsList.module.css";
import useUserContext from "../../hooks/useUserContext";
import {getUserNotifications} from "../../functions/api";
import {formatDate} from "../../functions/utils";
import Pagination from '@mui/material/Pagination';
import usePagination from '../../hooks/usePagination';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import {disableNotification, repeatNotification} from '../../functions/api'

const testData = [
    {
        id: 1,
        title: 'Programming',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In facilisis pretium mauris vel mattis. Phasellus ut augue auctor, lacinia magna a, efficitur nibh. Donec eget euismod mi, eu ullamcorper urna. Donec rhoncus sit amet lacus nec vehicula. Nullam non rutrum mauris. Ut convallis tortor sed est imperdiet, sed tristique risus dignissim. Praesent blandit rhoncus magna, a vulputate massa sagittis sit amet. Proin vitae porttitor turpis. Nam in molestie erat.',
        created_at: new Date().toString(),
        next_notifications: new Date().toString(),
    }]


const repeated = (id, setStatus, filterNotifications, token) => {
    console.log('Повторил');
    const clear = () => {
        filterNotifications(id);
    }
    clear();
    //repeatNotification(token, setStatus, clear);
}

const disable = (id, setStatus, filterNotifications, token) => {
    console.log('Убрал');
    const clear = () => {
        filterNotifications(id);
    }
    clear();
    // disableNotification(token, setStatus, clear)
}

const Notification = ({notification, setStatus, filterNotifications, token}) => {
    const {title, description, created_at, next_notifications, id} = notification;
    return (
        <div className={classes.container}>
            <div className={classes.notification_container}>
                <p>{title}</p>
                <p>{description}</p>
                <p>создано: {formatDate(created_at)}</p>
                <p>напоминание: {formatDate(next_notifications)}</p>
            </div>
            <div className={classes.button}>
                <button onClick={(e) => {
                    e.preventDefault();
                    repeated(id, setStatus, filterNotifications, token);
                }}>Повторил
                </button>
                <button onClick={(e) => {
                    e.preventDefault();
                    disable(id, setStatus, filterNotifications, token);
                }}>Больше не показывать
                </button>
            </div>
        </div>
    )
}

const NotificationList = () => {
    const [notifications, setNotifications] = useState([]);
    const {token, setStatusText, setModalStatus} = useUserContext();
    let [page, setPage] = useState(1);
    const PER_PAGE = 2;
    const count = Math.ceil(notifications.length / PER_PAGE);
    const _DATA = usePagination(notifications, PER_PAGE);
    const setStatus = (text) => {
        setStatusText(text);
        setModalStatus(true);
    }
    useEffect(() => {
        if (token) {
            getUserNotifications(token, setNotifications)
        }
    }, [token]);

    const filterNotifications = (id) => {
        const notification_ = notifications.filter(el => el.id !== id);
        setNotifications(notification_);
    }

    useEffect(() => {
        if(page > count){
            setPage(page - 1);
            _DATA.jump(page - 1);
        }
        else if(page <= 0){
            setPage(1);
            _DATA.jump(1);
        }
    }, [notifications]);

    const handleChange = (e, p) => {
        console.log(p);
        setPage(p);
        _DATA.jump(p);
    };

    const darkTheme = createTheme({
        palette: {
            mode: 'dark',
        },
    });

    const NotificationListRaw = () => {
        if (notifications.length !== 0) {
            return (
                <div>
                    <h2>Ваши напоминания</h2><br/>
                    <ThemeProvider theme={darkTheme}>
                        <Pagination
                            count={count}
                            page={page}
                            size="large"
                            color="primary"
                            variant="outlined"
                            // shape="rounded"
                            onChange={handleChange}
                        />
                    </ThemeProvider>
                    {_DATA.currentData().map((notification) =>
                        <Notification notification={notification}
                                      setStatus={setStatus}
                                      filterNotifications={filterNotifications}
                                      key={notification.id}
                                      token={token}
                        />)
                    }
                </div>
            )
        }
        return <h2>У вас пока нет активного напоминания.</h2>
    }

    return NotificationListRaw();

}


export default NotificationList;
