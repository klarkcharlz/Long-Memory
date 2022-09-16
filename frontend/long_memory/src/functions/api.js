import axios from "axios";

import {set_token_to_storage} from "./tokenStorage";
import {parseResponse} from "./utils"

import {URL, PORT, PROTOCOL} from './api_constants'


const GET_USER_NOTIFICATIONS_URL = `${PROTOCOL}://${URL}${PORT}/api/notifications/`;
const CREATE_NOTIFICATIONS_URL = `${PROTOCOL}://${URL}${PORT}/api/notifications/`;
const USER_REGISTRATION_URL = `${PROTOCOL}://${URL}${PORT}/api/register/`;
const USER_AUTHORIZATION_URL = `${PROTOCOL}://${URL}${PORT}/api/api-token-auth/`;
const GET_USER_DATA_URL = `${PROTOCOL}://${URL}${PORT}/api/user_data/`;
const DISABLE_NOTIFICATION_URL = `${PROTOCOL}://${URL}${PORT}/api/notifications/`;
const REPEAT_NOTIFICATION_URL = `${PROTOCOL}://${URL}${PORT}/api/notifications/`;
const USER_ACTIVATION_URL = `${PROTOCOL}://${URL}${PORT}/api/activate/`;
const BUG_REPORT_URL = `${PROTOCOL}://${URL}${PORT}/api/bug_report/`

function get_headers(token = null) {
    let headers = {
        'Content-Type': 'application/json'
    }
    if (token) {
        headers['Authorization'] = 'token ' + token
    }
    return headers
}


function sendBugReport(data, setStatus) {
    const headers = get_headers();
    axios.post(BUG_REPORT_URL, data, {headers})
        .then(response => {
            // console.log('sendBugReport response.data > ', response.data);
            setStatus("Отправлено.");
        }).catch((error) => {
        // console.log(error);
        setStatus('Извините, проблемы с сервером.');
    })
}


function getUserNotifications(token, setNotifications, endLoading, setStatus) {
    const headers = get_headers(token);
    axios.get(GET_USER_NOTIFICATIONS_URL, {headers})
        .then(response => {
            // console.log('getUserNotifications response.data > ', response.data);
            endLoading(false);
            const notifications = response.data;
            setNotifications(notifications);
        }).catch((error) => {
        console.error(error)
        setStatus('Извините, проблемы с сервером.')
        endLoading(false);
    })
}

function getUserData(setStatus, token, setUserData, endLoading) {
    const headers = get_headers(token);
    axios.get(GET_USER_DATA_URL, {headers})
        .then(response => {
            // console.log('getUserData response.data > ', response.data);
            endLoading(false)
            const userData = response.data;
            // setStatus("Информация получена.");
            setUserData(userData);
        }).catch((error) => {
        endLoading(false)
        setStatus('Извините, проблемы с сервером.');
        console.error(error)
    })
}

function createNotification(data, token, setStatus, clearForm) {
    const headers = get_headers(token);
    axios.post(CREATE_NOTIFICATIONS_URL, data, {headers})
        .then(response => {
            // console.log('createNotification response.data > ', response.data);
            clearForm();
            setStatus("Напоминание создано успешно.");
        }).catch((error) => {
        // console.log(error);
        setStatus('Извините, проблемы с сервером.');
    })
}

function updateUser(token, data, setStatus) {
    let delAvatar = false;
    const avatar = data.avatar;
    if (avatar === null || !data.avatar.startsWith('data:image')) {
        delete data.avatar;
        delAvatar = true;
    }
    const headers = get_headers(token);
    axios.patch(GET_USER_DATA_URL, data, {headers})
        .then(response => {
            // console.log('updateUser response.data > ', response.data);
            setStatus('Информация обновлена.');
        }).catch((error) => {
        // console.log(error);
        setStatus(parseResponse(error.response.data));
    })
    if (delAvatar) data.avatar = avatar;
}


function userRegistration(pass, username, email, navigate, setStatus, offDisabled, onDisabled) {
    const headers = get_headers();
    onDisabled();
    axios.post(USER_REGISTRATION_URL, {username: username, password: pass, email: email}, {headers})
        .then(response => {
            navigate("/authorization");
            setStatus('На вашу почту отправлено письмо с подтверждением регистрации.')
            offDisabled()
        }).catch((error) => {
        // console.log(error);
        setStatus(parseResponse(error.response.data));
        offDisabled();
    })
}

function userAuthorization(username, pass, setToken, navigate, setStatus) {
    const headers = get_headers();
    axios.post(USER_AUTHORIZATION_URL, {username: username, password: pass}, {headers})
        .then(response => {
            // console.log('userAuthorization response.data > ', response.data);
            const token = response.data.token;
            set_token_to_storage(token);
            setToken(token);
            navigate("/notifications_list");
        }).catch((error) => {
        // console.log(error);
        setStatus('Неправильный логин или пароль.');
    });
}

function disableNotification(token, id, setStatus, clear) {
    const headers = get_headers(token);
    axios.delete(`${DISABLE_NOTIFICATION_URL}${id}`, {headers})
        .then(response => {
            // console.log('disableNotification response.data > ', response.data);
            clear();
        }).catch((error) => {
        // console.log(error);
        setStatus(parseResponse(error.response.data))
    })
}

function repeatNotification(token, id, setStatus, clear) {
    const headers = get_headers(token);
    axios.patch(`${REPEAT_NOTIFICATION_URL}${id}`, {}, {headers})
        .then(response => {
            // console.log('repeatNotification response.data > ', response.data);
            clear();
        }).catch((error) => {
        // console.log(error);
        setStatus(parseResponse(error.response.data))
    })
}

function userActivation(uid, token, setStatus, navigate) {
    const headers = get_headers();
    const url = `${USER_ACTIVATION_URL}${uid}/${token}/`;
    axios.get(url,{headers})
        .then(response => {
            // console.log('userActivation response.data > ', response);
            const status = response.status;
            if (status === 201) {
                navigate("/authorization");
                setStatus("Учетная запись подтверждена.<br>Теперь Вы можете авторизоваться.");
            }
        }).catch((error) => {
        // console.log(error);
        navigate("/authorization");
        setStatus("Извините, проблемы с сервером или же ссылка уже не действительна.");
    });
}


export {
    repeatNotification,
    disableNotification,
    getUserData,
    updateUser,
    getUserNotifications,
    createNotification,
    userRegistration,
    userAuthorization,
    userActivation,
    sendBugReport
};