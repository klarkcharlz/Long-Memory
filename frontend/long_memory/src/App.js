import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import StartPage from "./components/StartPage/StartPage";
import Menu from "./components/Menu/Menu";
import NotFound from "./components/NotFound/NotFound";
import CreateNotification from "./components/CreateNotification/CreateNotification";
import NotificationList from "./components/NotificationsList/NotificationsList";
import AuthorizationForm from "./components/AuthorizationForm/AuthorizationForm";
import RegistrationForm from "./components/RegistrationForm/RegistrationForm";
import StatusModal from "./components/StatusModal/StatusModal"
import {get_token_from_storage} from "./functions/tokenStorage"
import classes from "./App.module.css";
import useUserContext from "./hooks/useUserContext";
import PersonalArea from './components/PersonalArea/PersonalArea'


export default function App() {
    const {setToken, modalStatus, setModalStatus, statusText} = useUserContext();

    useEffect(() => {
        const token = get_token_from_storage();
        setToken(token);
    }, []);

    return (
        <div className={classes.body}>
            <StatusModal open={modalStatus} setOpen={setModalStatus} status={statusText}/>
            <Router>
                <Header/>
                <div className={classes.container}>
                    <div className={classes.main}>
                        <div className={classes.router}>
                            <Routes>
                                <Route
                                    path="/main"
                                    element={<StartPage/>}
                                />
                                <Route
                                    path="/create_notification"
                                    element={<CreateNotification/>}
                                />
                                <Route
                                    path="/notifications_list"
                                    element={<NotificationList/>}
                                />
                                <Route
                                    path="/registration"
                                    element={<RegistrationForm/>}
                                />
                                <Route
                                    path="/authorization"
                                    element={<AuthorizationForm/>}
                                />
                                <Route
                                    path="/pa"
                                    element={<PersonalArea/>}
                                />
                                <Route
                                    path="*"
                                    element={<StartPage/>}
                                />
                            </Routes>
                        </div>
                        <div className={classes.menu}>
                            <Menu/>
                        </div>
                    </div>
                </div>
            </Router>
            <div>
                <Footer className={classes.footer}/>
            </div>
        </div>
    );
}
