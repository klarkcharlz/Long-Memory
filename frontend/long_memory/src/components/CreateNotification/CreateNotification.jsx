import React, { useState } from "react";


const createNotification = (title, description) => {
    console.log('Создано');
    console.log(title);
    console.log(description);
}


const CreateNotification = () => {
    const [title, setTitle] = useState('React hooks');
    const [description, setDescription] = useState('useState');
    return (
        <div>
            <form>
                <label> Тема(ы)
                    <input type="text"
                           name="title"
                           value={title}
                           onChange={(e) => {
                               setTitle(e.target.value)
                           }}
                    />
                </label>
                <br/>
                <label> Описание
                    <textarea
                        name="description"
                        value={description}
                        onChange={(e) => {
                            setDescription(e.target.value);
                        }}
                    />
                </label>
                <br/>
                <button type="button" onClick={() => {
                    createNotification(title, description);
                }}>Создать
                </button>
            </form>
        </div>
    )
}

// export default CreateNotification;
export default CreateNotification;
