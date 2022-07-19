import axios from "axios";

import {set_token_to_storage} from "./tokenStorage";

const GET_USER_NOTIFICATIONS_URL = `http://127.0.0.1:8000/api/notifications/`;
const CREATE_NOTIFICATIONS_URL = `http://127.0.0.1:8000/api/notifications/`;
const USER_REGISTRATION_URL = `http://127.0.0.1:8000/api/register/`;
const USER_AUTHORIZATION_URL = `http://127.0.0.1:8000/api-token-auth/`;


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

function createNotification(data, token) {
    const headers = get_headers(token);
    axios.post(CREATE_NOTIFICATIONS_URL, data, {headers})
        .then(response => {
            console.log('createNotification response.data > ', response.data);
        }).catch(error => console.error(error))
}

function userRegistration(pass, username, email, setToken, navigate) {
    axios.post(USER_REGISTRATION_URL, {username: pass, password: username, email: email})
        .then(response => {
            console.log('userRegistration response.data > ', response.data);
            const token = response.data.token;
            set_token_to_storage(token);
            setToken(token);
            navigate("/notifications_list");
            // getUserNotifications(token, setNotifications)
        }).catch(error => console.error(error))
}

function userAuthorization(pass, username, setToken, navigate) {
    axios.post(USER_AUTHORIZATION_URL, {username: pass, password: username})
        .then(response => {
            console.log('userAuthorization response.data > ', response.data);
            const token = response.data.token;
            set_token_to_storage(token);
            setToken(token);
            navigate("/notifications_list");
            // getUserNotifications(token, setNotifications)
        }).catch(error => console.error(error));
}

export {getUserNotifications, createNotification, userRegistration, userAuthorization};
