import React from 'react';
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";
import {useLocation} from "react-router-dom";


const VkAuth = () => {
    const {setToken} = useUserContext();
    const setStatus = useStatusModalHook();

    const search = "?" + window.location.hash.slice(1, window.location.hash.length)
    const queryParams = new URLSearchParams(search);
    const accessToken = queryParams.get('access_token');
    const userId = queryParams.get('user_id');
    const expiresIn = queryParams.get('expires_in');
    const email = queryParams.get('email');

    // console.log(accessToken);
    // console.log(userId);
    // console.log(expiresIn);
    // console.log(email);

    return (
        <div>
            <h1>Hello</h1>
        </div>
    );
};

export default VkAuth;