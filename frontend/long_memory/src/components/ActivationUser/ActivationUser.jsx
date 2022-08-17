import React from 'react';
import { useParams, useNavigate } from "react-router-dom";
import {userActivation} from '../../functions/api';
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";


const ActivationUser = () => {
    const {setToken} = useUserContext();
    const setStatus = useStatusModalHook();
    const {uid, token} = useParams();
    return (
        <div>
            <h1>Hello</h1>
            <h2>{uid}</h2>
            <h2>{token}</h2>
        </div>
    );
};

export default ActivationUser;