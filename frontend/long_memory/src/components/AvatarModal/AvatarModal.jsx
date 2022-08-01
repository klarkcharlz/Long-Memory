import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import classes from "./AvatarModal.module.css"

export default function AvatarModal({open, setOpen, children}) {
    const handleClose = () => setOpen(false);

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box className={classes.avatar_modal}>
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        {children}
                    </Typography>
                </Box>
            </Modal>
        </div>
    );
}
