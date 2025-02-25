import React, {useEffect, useState} from "react";
import classes from "./CreateNotification.module.css";
import {createNotification, getThemes} from "../../functions/api"
import useUserContext from "../../hooks/useUserContext";
import useStatusModalHook from "../../hooks/useStatusModalHook";


const validateUserInfo = (notification) => {
  let error = [];
  let validate;

  if (!notification.title) error.push("Заголовок не может быть пустой.");
  if (!notification.description) error.push("Описание не может быть пустым.");

  validate = error.length < 1;

  return [validate, error];
}

const createNotification_ = (title, description, theme, token, clearForm, setStatus) => {
  if (theme.id === 0) {
      theme = null;
    } else {
      theme = theme.id;
    }

  const notification = {
    title,
    description,
    theme
  }
  const [valid, error] = validateUserInfo(notification);
  if (valid) createNotification(notification, token, setStatus, clearForm);
  else setStatus(error.join('\n'));
}

const ThemeSelect = ({userThemes, theme, setTheme}) => {
  const [themes, setThemes] = useState(userThemes || [{id: 0, title: "Нету"}]);

  useEffect(() => {
     setThemes([{id: 0, title: "Нету"}, ...userThemes])
  }, [userThemes]);

  const saveTheme = (target) => {
    const selectedTheme = themes.find(t => t.title === target.value);
    if (selectedTheme) {
      setTheme(selectedTheme);
    }
  }

  return (
    <label style={{position: "relative", display: "flex"}}>
      <select style={{
        height: "3em",
        background: "#1b6d8580",
        border: "none",
        borderRadius: "10px",
        color: "white",
        paddingLeft: "20px",
        marginTop: "10px",
        outline: "none",
        width: "200px"
      }}
              value={theme.title}
              onChange={event => saveTheme(event.target)}
      >
        {themes.map(theme =>
          <option key={theme.id} value={theme.title}>
            {theme.title}
          </option>
        )}
      </select>
    </label>
  );
};


const CreateNotification = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [themes, setThemes] = useState([]);
  const [theme, setTheme] = useState({id: 0, title: "Нету"});
  const {token} = useUserContext();
  const clearForm = () => {
    setTitle("");
    setDescription("");
  }
  const setStatus = useStatusModalHook();

  const saveThemes = (themes) => {
    setThemes(themes);
  }

  useEffect(() => {
    if (token) {
      getThemes(token, saveThemes, setStatus)
    }
  }, [token]);

  if (!token) return <h1>Авторизуйтесь</h1>

  return (
    <div>
      <form className={classes.card_form}>
        <label className={classes.title_area}>Заголовок и тема
          <input
            className={classes.title_notification}
            type="text"
            name="title"
            placeholder={"React Hooks"}
            value={title}
            onChange={(e) => {
              setTitle(e.target.value)
            }}
          />
        </label>
        <ThemeSelect userThemes={themes} theme={theme} setTheme={(theme) => setTheme(theme)}/>
        <br/>
        <label className={classes.area_form}>Описание
          <textarea className={classes.theme_notification}
                    name="description"
                    placeholder={"useState"}
                    value={description}
                    onChange={(e) => {
                      setDescription(e.target.value);
                    }}
          />
        </label>
        <br/>
        <button className={classes.button} type="button" onClick={() => {
          createNotification_(title, description, theme, token, clearForm, setStatus);
        }}>СОЗДАТЬ
        </button>
      </form>
    </div>
  )
}

export default CreateNotification;
