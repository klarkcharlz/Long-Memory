import React, {useEffect, useMemo, useState} from "react";
import classes from "./NotificationsList.module.css";
import useUserContext from "../../hooks/useUserContext";
import {getUserNotifications} from "../../functions/api";
import {formatDate} from "../../functions/utils";
import Pagination from '@mui/material/Pagination';
import usePagination from '../../hooks/usePagination';
import {ThemeProvider, createTheme} from '@mui/material/styles';
import {disableNotification, repeatNotification} from '../../functions/api'
import useStatusModalHook from "../../hooks/useStatusModalHook";
import MySelect from "../MySelect/MySelect";
import Loader from "../Loader/Loader";


const testData = [
    {
        id: 1,
        title: 'Programming',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In facilisis pretium mauris vel mattis. Phasellus ut augue auctor, lacinia magna a, efficitur nibh. Donec eget euismod mi, eu ullamcorper urna. Donec rhoncus sit amet lacus nec vehicula. Nullam non rutrum mauris. Ut convallis tortor sed est imperdiet, sed tristique risus dignissim. Praesent blandit rhoncus magna, a vulputate massa sagittis sit amet. Proin vitae porttitor turpis. Nam in molestie erat.',
        created_at: new Date().toString(),
        next_notifications: new Date().toString(),
    }]


const repeated = (id, setStatus, filterNotifications, token) => {
    const clear = () => {
        filterNotifications(id);
    }
    repeatNotification(token, id, setStatus, clear);
}

const disable = (id, setStatus, filterNotifications, token) => {
    const clear = () => {
        filterNotifications(id);
    }
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
    const {token} = useUserContext();
    const [page, setPage] = useState(1);
    const setStatus = useStatusModalHook();

    const [isLoading, setIsLoading] = useState(false);
    const [filterText, setFilterText] = useState('');
    const [selectedSort, setSelectedSort] = useState('next_notifications');
    const PER_PAGE = 2;  // количество напоминаний на странице для пагинации


    const endLoading = () => {
        setIsLoading(false);
    }

    useEffect(() => {
        if (token) {
            setIsLoading(true);
            // getUserNotifications(token, setNotifications, endLoading, setStatus)
            setTimeout(() => {
                getUserNotifications(token, setNotifications, endLoading);
            }, 3000)
        }
    }, [token]);

    const filterSortedNotifications = useMemo(() => {
        return notifications.filter((el) => {
            return el.title.toLowerCase().includes(filterText.toLowerCase()) ||
                el.description.toLowerCase().includes(filterText.toLowerCase());
        })
    }, [filterText, notifications]);

    const count = Math.ceil(filterSortedNotifications.length / PER_PAGE);
    const _DATA = usePagination(filterSortedNotifications, PER_PAGE);

    useEffect(() => {
        if (page > count) {
            setPage(count);
            _DATA.jump(count);
        } else if (page <= 0) {
            setPage(1);
            _DATA.jump(1);
        }
        _DATA.jump(page);
    }, [filterSortedNotifications]);

    const filterNotifications = (id) => {
        const notification_ = notifications.filter(el => el.id !== id);
        setNotifications(notification_);
    }

    const sortList = (sort, direction) => {
        if (notifications.length >= 1) {
            console.log(notifications);
            console.log(sort);
            console.log(direction);
            setSelectedSort(sort);
            let notifications_ = [...notifications].sort((prev, cur) => {
                const prevDate = new Date(prev[sort]);
                const curDate = new Date(cur[sort]);
                // prev < cur
                if (prevDate < curDate) {
                    return -1
                }
                // prev > cur
                else if (prevDate > curDate) {
                    return 1
                }
                // prev == cur
                return 0;
            });
            if (direction === 'down') notifications_ = notifications_.reverse();
            setNotifications(notifications_);
        }
    }

    const handleChange = (e, p) => {
        setPage(p);
        _DATA.jump(p);
    };

    const darkTheme = createTheme({
        palette: {
            mode: 'dark',
        },
    });

    const NotificationListRaw = () => {
        if(isLoading) return <div style={{display: 'flex', justifyContent: 'center', marginTop: 150}}><Loader/></div>
        if (notifications.length !== 0) {
            return (
                <div>
                    <h2>Ваши напоминания</h2><br/>

                    <div className={classes.filter_sorted}>
                        <input className={classes.filter}
                               type='text'
                               placeholder='поиск'
                               value={filterText}
                               onChange={event => setFilterText(event.target.value)}
                        />
                        <MySelect
                            value={selectedSort}
                            onChange={sortList}
                            defaultValue={selectedSort}
                            options={[
                                {value: 'created_at', name: 'по дате создания'},
                                {value: 'next_notifications', name: 'по дате напоминания'},
                            ]}
                        />
                    </div>
                    <br/>

                    <ThemeProvider theme={darkTheme}>
                        <Pagination
                            count={count}
                            page={page}
                            size="large"
                            color="primary"
                            variant="outlined"
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
