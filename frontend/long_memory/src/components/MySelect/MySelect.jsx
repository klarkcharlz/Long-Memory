import React from 'react';
import classes from "./MySelect.module.css"

const MySelect = ({options, defaultValue, value, onChange}) => {
    return (
        <label className={classes.sorted__icon}>
            <select className={classes.sorted}
                    value={value}
                    onChange={event => onChange(event.target.value)}
            >
                <option disabled value="">{defaultValue}</option>
                {options.map(option =>
                    <option key={option.value} value={option.value}>
                        {option.name}
                    </option>
                )}
            </select>
        </label>
    );
};

export default MySelect;
