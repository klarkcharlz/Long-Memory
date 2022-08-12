import React, {useEffect, useState} from 'react';
import classes from "./MySelect.module.css"
import ArrowCircleUpIcon from "@mui/icons-material/ArrowCircleUp";
import ArrowCircleDownIcon from "@mui/icons-material/ArrowCircleDown";


const MySelect = ({options, defaultValue, onChange}) => {
    const [value_, setValue] =useState(defaultValue);
    const [sortingDirection, setSortingDirection] = useState('up');
    const [arrow, setArrow] = useState(<ArrowCircleDownIcon/>);

    useEffect(() => {
        onChange(value_, sortingDirection);
    }, [value_, sortingDirection]);

    return (
        <label className={classes.sorted__icon}>
            <select className={classes.sorted}
                    value={value_}
                    onChange={event => setValue(event.target.value)}
            >
                <option disabled value={defaultValue}>по дате напоминания</option>
                {options.map(option =>
                    <option key={option.value} value={option.value}>
                        {option.name}
                    </option>
                )}
            </select>
            <div className={classes.sorted_up} onClick={(e) => {
                console.log('click arrow');
                e.stopPropagation();
                if (sortingDirection === 'up') {
                    setSortingDirection('down');
                    setArrow(<ArrowCircleUpIcon/>);
                } else if (sortingDirection === 'down') {
                    setSortingDirection('up');
                    setArrow(<ArrowCircleDownIcon/>);
                }
            }}>
                {arrow}
            </div>
        </label>
    );
};

export default MySelect;
