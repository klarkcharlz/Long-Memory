import useUserContext from "./useUserContext";

const useStatusModalHook = () => {
    const {setStatusText, setModalStatus} = useUserContext();
    return (text) => {
        setStatusText(text)
        setModalStatus(true);
    }
};

export default useStatusModalHook;
