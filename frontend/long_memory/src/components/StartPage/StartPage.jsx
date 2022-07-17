import React from "react";
import classes from "./StartPage.module.css";


const StartPage = () => {
    return (
        <div className={classes.start_page}>
            <h3>Welcome to the long-term memory training website</h3>
            <p>Write down what you learned today.<br/>And on the site you can see reminders of what needs to be repeated.</p>
            <br/>
            <ul className={classes.list}>
                <li>
                    <p>In one day.</p>
                </li>
                <li>
                    <p>In 3 days.</p>
                </li>
                <li>
                    <p>A week later.</p>
                </li>
                <li>
                    <p>In 3 weeks.</p>
                </li>
                <li>
                    <p>In a month.</p>
                </li>
                <li>
                    <p>In 3 months.</p>
                </li>
                <li>
                    <p>After half a year.</p>
                </li>
            </ul>
            <br/>
            <p>P.S. each new reminder counts down the time from the previous one.</p>
            <p>Try every time to remember everything from memory from your head to the maximum,
                and what you do not remember carefully repeat.</p>
        </div>
    )
}

export default StartPage;
