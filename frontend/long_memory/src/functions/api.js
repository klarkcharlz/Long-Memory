import axios from "axios";

const GET_USER_NOTIFICATIONS_URL = `http://127.0.0.1:5000`;
const CREATE_NOTIFICATIONS_URL = `http://127.0.0.1:5000`;
const USER_REGISTRATION_URL = `http://127.0.0.1:5000`;
const USER_AUTHORIZATION_URL = `http://127.0.0.1:5000`;

function getUserNotifications() {
    axios.get(GET_USER_NOTIFICATIONS_URL)
        .then(response => {
            console.log('response.data > ', response.data);
            const notifications = response.data;
        }).catch(error => console.error(error))
}

function createNotification(data) {
    // {title, description}
    axios.post(CREATE_NOTIFICATIONS_URL, data)
        .then(response => {
            console.log(response.data);
        }).catch(error => console.error(error))
}

function userRegistration() {
    // {username, email, password}
    axios.get(USER_REGISTRATION_URL)
        .then(response => {
            console.log('response.data > ', response.data);
            const notifications = response.data;
        }).catch(error => console.error(error))
}

function userAuthorization() {
    // {username, password}
    axios.get(USER_AUTHORIZATION_URL)
        .then(response => {
            console.log('response.data > ', response.data);
            const notifications = response.data;
        }).catch(error => console.error(error))
}

export {getUserNotifications, createNotification};
