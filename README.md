# Long-Memory

## Backend:

+ Перейти в каталог:
    + cd backend/long_memory/long_memory/

+ Перед работой установите все зависимости из requirements.txt:
    + pip install -r requirements.txt

+ Устанавливая новые пакеты добавляйте их в requirements.txt:
    + pip freeze > requirements.txt

+ Скачав проект создайте и примените миграции, так же создайте суперпользователя.
    + python manage.py makemigrations
    + python manage.py migrate
    + python manage.py createsuperuser

Если у вас какие-то проблемы с миграциями попробуйте удалить все файлы из папок с миграциями кроме __init__.py
и удалите базу данных если у вас sqlite, если у вас postgresql в контейнере удалите контейнер и запустите заново,
после чего повторите создание миграций.


## frontend

+ Перейти в каталог:
    + cd frontend/long_memory/

+ Перед работой установите все зависимости
    + npm install

+ Запуск проекта:
    + npm start

+ Сборка проекта:
    + npm run build

## P.S.
Создавая и добавляя в проект какие-то файлы которые вам нужны для разработки 
и тестирования не забудьте добавить их в .gitignore.

