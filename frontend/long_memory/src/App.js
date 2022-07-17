import React, {useState} from 'react';
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
import TestComponent from "./components/TestComponent/TestComponent"

import classes from "./App.module.css";

export default function App() {
    const [token, setToken] = useState(false);
    const [modalStatus, setModalStatus] = useState(false);
    return (
        <div className={classes.body}>
            <Router>
                {token ? <p>Вы авторизованы</p> : <p>Вы не авторизованы</p>}
                <Header token={token} setToken={setToken}/>
                <TestComponent/>
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
                                path="*"
                                element={<NotFound/>}
                            />
                        </Routes>
                    </div>
                    <div className={classes.menu}>
                        <Menu token={token}/>
                    </div>
                </div>
            </Router>
            <StatusModal status="Все плохо!" modalStatus={modalStatus} setModalStatus={setModalStatus}/>
            <Footer className={classes.footer}/>
        </div>
    );
}
