import React from "react";
import classes from "./Footer.module.css";
import useContentModalHook from "../../hooks/useContentModalHook";
import BugReportForm from "../BugReportForm/BugReportForm";

const Footer = () => {
    const openBugReportForm = useContentModalHook();

    return (
        <div className={classes.footer}>
            <div className={classes.footerItem}>
                <a href="https://vk.com/public214673853" rel="noreferrer" target="_blank">
                    <svg className={classes.logo_vk}></svg>
                </a>
                <h5>crazy-pythons-crew © 2022</h5>
            </div>
            <div onClick={(e) => {
                openBugReportForm(<BugReportForm/>);
            }}>
                <h5 className={classes.bugReport}>Сообщить о проблеме</h5>
            </div>
        </div>
    )
}

export default Footer;
