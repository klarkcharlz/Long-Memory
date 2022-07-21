import React from "react";


const PersonalArea = () => {
    return (
        <div>
            <div>
                <img src="https://mir-avatarok.3dn.ru/_si/0/43720430.jpg" alt="Аватар"/>
            </div>
            <div>
                <table>
                    <caption>Настройка уведомлений</caption>
                    <thead>
                    <tr>
                        <th></th>
                        <th>Согласие на рассылку</th>
                        <th>id/email</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Telegram</td>
                        <td><input type="checkbox"/></td>
                        <td><input type="text"/></td>
                        <td>
                            <button>Сохранить</button>
                        </td>
                    </tr>
                    <tr>
                        <td>Вк</td>
                        <td><input type="checkbox"/></td>
                        <td><input type="text"/></td>
                        <td>
                            <button>Сохранить</button>
                        </td>
                    </tr>
                    <tr>
                        <td>Электронная почта</td>
                        <td><input type="checkbox"/></td>
                        <td><input type="email"/></td>
                        <td>
                            <button>Сохранить</button>
                        </td>
                    </tr>
                    </tbody>
                </table>

            </div>
            <hr/>
            <div>
                <table>
                    <caption>Дополнительные данные</caption>
                    <tbody>
                    <tr>
                        <td>Ваше Имя</td>
                        <td><input type="text"/></td>
                        <td>
                            <button>Сохранить</button>
                        </td>
                    </tr>
                    <tr>
                        <td>Аватар</td>
                        <td><input type="file"/></td>
                        <td>
                            <button>Сохранить</button>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
    )
}

export default PersonalArea;
