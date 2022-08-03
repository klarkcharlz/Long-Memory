import React, {useEffect, useMemo, useState} from "react";
import classes from "./NotificationsList.module.css";
import useUserContext from "../../hooks/useUserContext";
import {getUserNotifications} from "../../functions/api";
import {formatDate} from "../../functions/utils";
import Pagination from '@mui/material/Pagination';
import usePagination from '../../hooks/usePagination';
import {ThemeProvider, createTheme} from '@mui/material/styles';
import {disableNotification, repeatNotification} from '../../functions/api'
import ArrowCircleDownIcon from '@mui/icons-material/ArrowCircleDown';
import ArrowCircleUpIcon from '@mui/icons-material/ArrowCircleUp';

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
    // clear();
    repeatNotification(token, id, setStatus, clear);
}

const disable = (id, setStatus, filterNotifications, token) => {
    console.log('Убрал');
    const clear = () => {
        filterNotifications(id);
    }
    // clear();
    disableNotification(token, id, setStatus, clear)
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
    const [searchText, setSearchText] = useState('');
    const {token, setStatusText, setModalStatus} = useUserContext();
    const [page, setPage] = useState(1);
    const [sorted, setSorted] = useState('up');
    const [arrow, setArrow] = useState(<ArrowCircleDownIcon/>);

    const PER_PAGE = 2;

    const setStatus = (text) => {
        setStatusText(text);
        setModalStatus(true);
    }

    useEffect(() => {
        if (token) {
            getUserNotifications(token, setNotifications)
        }
    }, [token]);

    const sortedAndSearchNotifications = useMemo(() => {
        console.log('работаем');
        return notifications.filter((el) => {
            return el.title.toLowerCase().includes(searchText.toLowerCase());
        }).sort((prev, cur) => {
            // нужно преобразовать строку в дату и в ифах сравнивать даты
            // const prevDate = prev.next_notifications;
            // const curDate = cur.next_notifications;
            // prev < cur
            if (1) {
                return -1;
            }
            // prev > cur
            else if (1) {
                return 1;
            }
            // prev == cur
            return 0;
        });
    }, [searchText, notifications, sorted]);

    useEffect(() => {
        if (page > count) {
            setPage(count);
            _DATA.jump(count);
        } else if (page <= 0) {
            setPage(1);
            _DATA.jump(1);
        }
    }, [sortedAndSearchNotifications]);

    const count = Math.ceil(sortedAndSearchNotifications.length / PER_PAGE);
    const _DATA = usePagination(sortedAndSearchNotifications, PER_PAGE);

    const filterNotifications = (id) => {
        const notification_ = notifications.filter(el => el.id !== id);
        setNotifications(notification_);
    }

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

                    <div>
                        <input
                            type="text"
                            placeholder='Поиск'
                            value={searchText}
                            onChange={(e) => {
                                setSearchText(e.target.value);
                            }}
                        />

                        <div onClick={(e) => {
                            e.stopPropagation();
                            if (sorted === 'up') {
                                setSorted('down');
                                setArrow(<ArrowCircleUpIcon/>);
                            } else if (sorted === 'down') {
                                setSorted('up');
                                setArrow(<ArrowCircleDownIcon/>);
                            }
                        }}>
                            {arrow}
                        </div>

                    </div>

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
