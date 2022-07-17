import {useContext} from "react";

import {UserContext} from "../components/UserProvider/UserProvider";

const useUserContext = () => useContext(UserContext);

export default useUserContext;
