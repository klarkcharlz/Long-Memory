import useUserContext from "./useUserContext";

const useContentModalHook = () => {
    const {setModalContent, setModalStatus, setStatusText} = useUserContext();
    return (component) => {
        setStatusText('');
        setModalContent(component)
        setModalStatus(true);
    }
};

export default useContentModalHook;
