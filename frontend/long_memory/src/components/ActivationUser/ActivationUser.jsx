import React, {useEffect} from 'react';
import {useParams, useNavigate} from "react-router-dom";
import {userActivation} from '../../functions/api';
import useStatusModalHook from "../../hooks/useStatusModalHook";
import Loader from "../Loader/Loader";

const userActivation_ = (uid, token, setStatus, navigate) => {
    // console.log(uid)
    // console.log(token)
    userActivation(uid, token, setStatus, navigate)
}


const ActivationUser = () => {
    const setStatus = useStatusModalHook();
    const {uid, token} = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        userActivation_(uid, token, setStatus, navigate);
    }, []);

    return (
        <div>
            <h1>Активация учетной записи...</h1>
            <div style={{display: 'flex', justifyContent: 'center', marginTop: 150}}>
                <Loader/>
            </div>
        </div>

    );
};

export default ActivationUser;