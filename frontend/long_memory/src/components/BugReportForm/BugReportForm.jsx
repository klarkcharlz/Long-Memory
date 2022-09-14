import React, {useState} from 'react';
import classes from "./BugReportForm.module.css";
import {sendBugReport} from "../../functions/api";
import useStatusModalHook from "../../hooks/useStatusModalHook";
import {Tooltip} from "@mui/material";
import {ThemeProvider, createTheme} from '@mui/material/styles';

const sendReport = (name, contacts, report, setStatus) => {
    const reportData = {
        user_name: name,
        contacts: contacts,
        description: report
    };
    sendBugReport(reportData, setStatus);
}

const theme = createTheme({
    components: {
        MuiTooltip: {
            styleOverrides: {
                tooltip: {
                    color: 'white',
                    transform: 'scale(1.5) !important',
                    backgroundColor: '#7FBCF0',
                    border: '1px solid #CCCFD2'
                }
            },
        },
    },
});

const BugReportForm = () => {
    const [name, setName] = useState('');
    const [contacts, setContacts] = useState('');
    const [report, setReport] = useState('');

    const [nameTooltip, setNameTooltip] = useState(false);
    const [reportTooltip, setReportTooltip] = useState(false);

    const setStatus = useStatusModalHook();



    return (
        <div className={classes.container}>
            <ThemeProvider theme={theme}>
                <form className={classes.card_form}>
                    <label className={classes.name_area}>
                        Как к Вам обращаться ?
                        <Tooltip open={nameTooltip}
                                 placement={'top'}
                                 title="Обязательное поле.">
                            <input
                                className={classes.name_input}
                                type="text"
                                value={name}
                                onChange={(e) => {
                                    setName(e.target.value)
                                }}
                                name="name"/>
                        </Tooltip>
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
                        <Tooltip open={reportTooltip}
                                 placement={'top'}
                                 title="Обязательное поле.">
                            <textarea
                                className={classes.textarea_input}
                                value={report}
                                name="report"
                                onChange={(e) => {
                                    setReport(e.target.value)
                                }}>
                            </textarea>
                        </Tooltip>
                    </label>
                    <br/>
                    <button
                        className={classes.button}
                        onClick={(e) => {
                            e.preventDefault();
                            let err = false;
                            if(!name.trim()){
                                err = true;
                                setNameTooltip(true);
                                setTimeout(() => setNameTooltip(false), 1500);
                            }
                            if(!report.trim()){
                                err = true;
                                setReportTooltip(true);
                                setTimeout(() => setReportTooltip(false), 1500);
                            }
                            if(err) return null;
                            sendReport(name, contacts, report, setStatus);
                        }}
                        type="button">
                        Отправить
                    </button>
                </form>
            </ThemeProvider>
        </div>
    );
};

export default BugReportForm;