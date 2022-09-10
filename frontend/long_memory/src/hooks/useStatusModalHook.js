import useUserContext from "./useUserContext";
import React from "react";

const useStatusModalHook = () => {
    const {setStatusText, setModalStatus, setModalContent} = useUserContext();
    return (text) => {
        setModalContent(<></>);
        setStatusText(text)
        setModalStatus(true);
    }
};

export default useStatusModalHook;
