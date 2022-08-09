import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    color: 'white',
    bgcolor: '#1b6d8580',
    // boxShadow: '5px 5px 100px rgba(61,61,61,0.5)',
    // border: '4px inset #08baad',
    border: '4px inset white',
    borderRadius: '25px',
    opacity: '0.8',
    // boxShadow: 24,
    textAlign: 'center',
    p: 4,
};

export default function StatusModal({open, setOpen, status}) {
    const handleClose = () => setOpen(false);

    function createMarkup() {
        return {__html: status};
    }

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Typography
                        dangerouslySetInnerHTML={createMarkup()}
                        id="modal-modal-title" variant="h6" component="h2">
                    </Typography>
                </Box>
            </Modal>
        </div>
    );
}
