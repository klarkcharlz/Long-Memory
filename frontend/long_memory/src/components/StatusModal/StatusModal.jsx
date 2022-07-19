import React from 'react';
import classes from "./StatusModal.module.css"


const StatusModal = ({modalStatus, setModalStatus, status}) => {
    return (
        <div className={modalStatus ? `${classes.modal} ${classes.modal_active}` : classes.modal}>
            <div className={modalStatus ? `${classes.modal_content} ${classes.modal_content_active}` : classes.modal_content} onClick={(e) => {
                setModalStatus(false)
            }}>
                <h2>{status}</h2>
            </div>
        </div>
    )
}


export default StatusModal;

