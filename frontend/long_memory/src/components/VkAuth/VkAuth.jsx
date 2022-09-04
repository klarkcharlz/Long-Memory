import React from 'react';
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";
import {useLocation} from "react-router-dom";
import {get_headers} from '../../functions/api';
import {useNavigate} from "react-router-dom";
import axios from "axios";
import {set_token_to_storage} from "../../functions/tokenStorage";
import {parseResponse} from "../../functions/utils"
import {URL, PORT} from '../../functions/api_constants'

const USER_AUTHORIZATION_URL = `http://${URL}${PORT}/auth/convert-token`;

const VkAuth = () => {
    const {setToken} = useUserContext();
    const setStatus = useStatusModalHook();
    const search = "?" + window.location.hash.slice(1, window.location.hash.length)
    const queryParams = new URLSearchParams(search);
    const navigate = useNavigate();
    const accessToken = queryParams.get('access_token');
    const userId = queryParams.get('user_id');
    const expiresIn = queryParams.get('expires_in');
    const email = queryParams.get('email');

    const headers = get_headers();
    const data = {
        grant_type:'convert_token',
        client_id: 'ITEQN4Vn0aGHzN7zvZTsYAHIhnE6tC0ATf9JTUDq',
        backend:'vk-oauth2',
        token:accessToken
        }
    axios.post(USER_AUTHORIZATION_URL, data, {headers})
         .then(response => {
             console.log('userAuthorization response.data > ', response.data);
             const token = response.data.access_token;
             console.log(token)
             set_token_to_storage(token);
             setToken(token);
             navigate("/notifications_list");
         }).catch((error) => {
         console.log(error);
         setStatus(parseResponse(error.response.data));

     });








//     console.log(accessToken);
//     console.log(userId);
//     console.log(expiresIn);
//     console.log(email);

    return (
        <div>
            <h1>Hello</h1>
        </div>
    );
};

export default VkAuth;