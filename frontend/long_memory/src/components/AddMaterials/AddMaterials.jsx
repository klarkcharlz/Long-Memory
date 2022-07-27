import React from 'react';
import classes from './AddMaterials.module.css'

const AddMaterials = () => {
    return (
        <div className={classes.add_materials}>
            <h2>Что такое кривая забывания</h2>
            <p>полная версия статьи
                <a href="https://externat.foxford.ru/polezno-znat/forgetting-curve?ysclid=l5loprx8xl217441546"
                   rel="noreferrer" target="_blank"> здесь</a>
            </p>
            <br/>
            <p>
                В конце XIX века немецкий психолог Герман Эббингауз сформулировал концепцию «кривой забывания» в
                монографии «Память». Он проводил опыты на себе и студентах: нужно было заучить бессмысленные слоги,
                используя разные техники запоминания. Сам Эббингауз фиксировал время и наблюдал, как скоро испытуемые
                забудут эту информацию.

                Оказалось, что после первых 20 минут студенты помнили 60% слогов, спустя девять часов — 40%, а через
                месяц — чуть больше 20% заученного. Эта зависимость получила название <b>кривой забывания Эббингауза</b>
            </p>
            {/*<br/>*/}
            {/*<img src="../Static/Ebbinghaus.png" alt="Кривая Эббингауза"/>*/}
            <br/>
            <p>
                Учёный провёл второй эксперимент для сравнения результатов. На этот раз нужно было заучивать не
                бессмысленные слоги, а связный текст «Дон Жуана» Байрона, равный по объёму. Результат оказался примерно
                таким же — со временем удавалось воспроизводить меньшее количество информации. Именно поэтому даже
                отличники за лето порой забывают программу прошлого класса.

                В 2015 году нидерландские учёные Джаап Мурр и Джори Дрос подтвердили концепцию Эббингауза.
            </p><br/>
            <h2>Смотрите также:</h2>
            <ul>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D1%8C"
                       rel="noreferrer" target="_blank">Память</a>
                </li>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%AD%D1%84%D1%84%D0%B5%D0%BA%D1%82_%D0%BA%D1%80%D0%B0%D1%8F_(%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D1%8C)"
                       rel="noreferrer" target="_blank">Эффект края (память)</a>
                </li>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%B2%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D1%8F"
                       rel="noreferrer" target="_blank">Интервальные повторения</a>
                </li>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%BE%D0%B1%D1%83%D1%87%D0%B0%D0%B5%D0%BC%D0%BE%D1%81%D1%82%D0%B8"
                       rel="noreferrer" target="_blank">Кривая обучаемости</a>
                </li>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%BD%D0%B0%D0%BA%D0%BE%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B8_%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B9"
                       rel="noreferrer" target="_blank">Закон накопления и распределения повторений</a>
                </li>
                <li>
                    <a href="https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B_%D0%B8%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_%D0%BF%D0%B0%D0%BC%D1%8F%D1%82%D0%B8_%D0%AD%D0%B1%D0%B1%D0%B8%D0%BD%D0%B3%D0%B0%D1%83%D0%B7%D0%B0"
                       rel="noreferrer" target="_blank">Классические методы исследования памяти Эббингауза </a>
                </li>
            </ul>

        </div>
    );
};

export default AddMaterials;

// rsc + tab