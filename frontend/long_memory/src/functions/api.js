import axios from "axios";

import {set_token_to_storage} from "./tokenStorage";
import {parseResponse} from "./utils"

const GET_USER_NOTIFICATIONS_URL = `http://127.0.0.1:8000/api/notifications/`;
const CREATE_NOTIFICATIONS_URL = `http://127.0.0.1:8000/api/notifications/`;
const USER_REGISTRATION_URL = `http://127.0.0.1:8000/api/register/`;
const USER_AUTHORIZATION_URL = `http://127.0.0.1:8000/api-token-auth/`;
const GET_USER_DATA_URL = `http://127.0.0.1:8000/api/user_data/`;
const DISABLE_NOTIFICATION_URL = ``
const REPEAT_NOTIFICATION_URL = ``


function get_headers(token) {
    let headers = {
        'Content-Type': 'application/json'
    }
    if (token) {
        headers['Authorization'] = 'token ' + token
    }
    return headers
}


function getUserNotifications(token, setNotifications) {
    const headers = get_headers(token);
    axios.get(GET_USER_NOTIFICATIONS_URL, {headers})
        .then(response => {
            console.log('getUserNotifications response.data > ', response.data);
            const notifications = response.data;
            setNotifications(notifications);
        }).catch(error => console.error(error))
}

function getUserData(setStatus, token, setUserData) {
    const headers = get_headers(token);
    axios.get(GET_USER_DATA_URL, {headers})
        .then(response => {
            console.log('getUserData response.data > ', response.data);
            const userData = response.data;
            setStatus("Информация получена.");
            setUserData(userData);
        }).catch((error) => {
        setStatus(parseResponse(error.response.data));
        console.error(error)
    })
}

function createNotification(data, token, setStatus) {
    const headers = get_headers(token);
    axios.post(CREATE_NOTIFICATIONS_URL, data, {headers})
        .then(response => {
            console.log('createNotification response.data > ', response.data);
            setStatus("Напоминание создано успешно.");
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data));
    })
}

function updateUser(token, data, setStatus) {
    const avatar = data.avatar;
    delete data.avatar;
    const headers = get_headers(token);
    axios.patch(GET_USER_DATA_URL, data, {headers})
        .then(response => {
            console.log('updateUser response.data > ', response.data);
            setStatus('Информация обновлена.');
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data));
    })
    data.avatar = avatar;
}


function userRegistration(pass, username, email, setToken, navigate, setStatus) {
    axios.post(USER_REGISTRATION_URL, {username: username, password: pass, email: email})
        .then(response => {
            console.log('userRegistration response.data > ', response.data);
            const token = response.data.token;
            set_token_to_storage(token);
            setToken(token);
            navigate("/notifications_list");
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data))
    })
}

function userAuthorization(username, pass, setToken, navigate, setStatus) {
    axios.post(USER_AUTHORIZATION_URL, {username: username, password: pass})
        .then(response => {
            console.log('userAuthorization response.data > ', response.data);
            const token = response.data.token;
            set_token_to_storage(token);
            setToken(token);
            navigate("/notifications_list");
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data));
    });
}

function disableNotification(token, setStatus, clear) {
    const headers = get_headers(token);
    const data = {
        is_active: false
    }
    axios.patch(DISABLE_NOTIFICATION_URL, data, {headers})
        .then(response => {
            console.log('disableNotification response.data > ', response.data);
            clear();
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data))
    })
}

function repeatNotification(token, setStatus, clear) {
    const headers = get_headers(token);
    axios.get(REPEAT_NOTIFICATION_URL, {headers})
        .then(response => {
            console.log('repeatNotification response.data > ', response.data);
            clear();
        }).catch((error) => {
        console.log(error);
        setStatus(parseResponse(error.response.data))
    })
}

export {repeatNotification, disableNotification, getUserData, updateUser, getUserNotifications, createNotification, userRegistration, userAuthorization};
