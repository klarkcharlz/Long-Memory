import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import StartPage from "./components/StartPage/StartPage";
import Menu from "./components/Menu/Menu";
import NotFound from "./components/NotFound/NotFound";
import CreateNotification from "./components/CreateNotification/CreateNotification";
import NotificationList from "./components/NotificationsList/NotificationsList";
import classes from "./App.module.css";

export default function App() {
    return (
        <div className={classes.body}>
            <Router>
                <Header/>
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
                                path="*"
                                element={<NotFound/>}
                            />
                        </Routes>
                    </div>
                    <div className={classes.menu}>
                        <Menu/>
                    </div>
                </div>
            </Router>
            <Footer className={classes.footer}/>
        </div>
    );
}
