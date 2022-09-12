import React, {useState} from 'react';
import classes from "./BugReportForm.module.css";
import {sendBugReport} from "../../functions/api";
import useStatusModalHook from "../../hooks/useStatusModalHook";

const sendReport = (name, contacts, report, setStatus) => {
    const reportData = {
        user_name: name,
        contacts: contacts,
        description: report
    };
    // console.log(reportData);
    sendBugReport(reportData, setStatus);
}

const BugReportForm = () => {
    const [name, setName] = useState('');
    const [contacts, setContacts] = useState('');
    const [report, setReport] = useState('');

    const setStatus = useStatusModalHook();

    return (
        <div className={classes.container}>
            <form className={classes.card_form}>
                <label className={classes.name_area}>
                    Как к Вам обращаться ?
                    <input
                        className={classes.name_input}
                        type="text"
                        required={true}
                        value={name}
                        onChange={(e) => {
                            setName(e.target.value)
                        }}
                        name="name"/>
                </label>
                <br/>
                <label className={classes.text_area}>
                    Контакты для связи:
                    <textarea
                        className={classes.textarea_input}
                        value={contacts}
                        onChange={(e) => {
                            setContacts(e.target.value)
                        }}
                        name="contacts">
                    </textarea>
                </label>
                <br/>
                <label className={classes.text_area}>
                    В чем проблема ?
                    <textarea
                        className={classes.textarea_input}
                        value={report}
                        name="report"
                        onChange={(e) => {
                            setReport(e.target.value)
                        }}
                        required={true}>
                    </textarea>
                </label>
                <br/>
                <button
                    className={classes.button}
                    onClick={(e) => {
                        e.preventDefault();
                        sendReport(name, contacts, report, setStatus);
                    }}
                    type="button">
                    Отправить
                </button>
            </form>
        </div>
    );
};

export default BugReportForm;