import axios from "axios";

function getContent(dispatch) {
    axios.get(`http://127.0.0.1:5000`)
        .then(response => {
            console.log('response.data > ', response.data);
            const notifications = response.data;
        }).catch(error => console.error(error))
}

function setData(data) {
    axios.post(`http://127.0.0.1:5000`, data)
        .then(response => {
            console.log(response.data);
        }).catch(error => console.error(error))
}

export {getContent, setData};
