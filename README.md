# Long-Memory
## Развертывание проекта на новой машине:
  + Установить свежие версии Docker и Docker-Compose
  + Установить NodeJS
  + Создать переменные окружения ADMIN_LOGIN и ADMIN_PASS, убедиться что система их видит.
  + Склонировать проект.
  + Везде где есть .env.example создать и заполнить файлы .env
  + Заполнить frontend/long_memory/src/functions/api_constants.js  
  + Собрать фронт:
    + cd frontend/long_memory/
    + npm install
    + npm run build
  + В корне проекта создать папку www, в ней папки media и static. В папке media создать папку users_avatars.
  + В корне проекта создать папку postgresql.
  + скопировать содержимое папки frontend/long_memory/build/static в папку www/static
  + Собрать и запустить проект:
    + docker-compose build
    + docker-compose up -d

## Разработка

## Backend(Запуск вне контейнера)
+ Перейти в каталог:
    + `cd backend/long_memory/`

+ Перед работой установите все зависимости из requirements.txt:
    + `pip install -r requirements.txt`

+ Устанавливая новые пакеты добавляйте их в requirements.txt:
    + `pip freeze > requirements.txt` (лучше конечно подчищать от лишних зависимостей, которые подтягиваются самими модулями нужными для их работы.)

+ Скачав проект создайте и примените миграции, так же создайте суперпользователя.
    + `python manage.py makemigrations`
    + `python manage.py migrate`
    + `python manage.py createsuperuser`
  
+ Запуск сервера:
    + `python manage.py runserver`

Если у вас какие-то проблемы с миграциями попробуйте удалить все файлы из папок с миграциями кроме __init__.py
и удалите базу данных если у вас sqlite, если у вас postgresql в контейнере удалите контейнер и запустите заново,
после чего повторите создание миграций.


## Frontend(Запуск вне контейнера)

+ Перейти в каталог:
    + `cd frontend/long_memory/`

+ Перед работой установите все зависимости
    + `npm install`

+ Запуск проекта:
    + `npm start`

+ Сборка проекта:
    + `npm run build`
  
## SQLAlchemy.
+ Автоматическая генерация моделей для SQLAlchemy:
    + Необходима утилита sqlacodegen.
    + В терминале: sqlacodegen <DSN> > models.py 
    + Открыть файл и убрать ручками лишнее.

## Docker Compose.
+ Команды:
    + `docker-compose ps` - список всех запущенных контейнеров
    + `docker-compose stop <имя контейнера>` - остановить контейнер
    + `docker-compose build <имя контейнера>` - пересобрать контейнер
    + `docker-compose up -d <имя контейнера>` - запустить контейнер
    + `docker-compose rm <имя контейнера>` - удалить контейнер
    + `stop/build/up/rm` без указания контейнера сработает на все. 

Так же читайте комментарии в файлах settings.py какие значения констант для локального запуска использовать, а какие для контейнеров.
  
## P.S.
+ Создавая и добавляя в проект какие-то файлы которые вам нужны для разработки 
и тестирования не забудьте добавить их в .gitignore.
+ Если будете перезапускать контейнер с фронтом после изменений, не забудьте прежде чем билдить контейнер сбилдить проект: `npm run build`
+ Пример перезапуска определенного контейнера после изменений:
    + `docker-compose stop nginx`
    + `docker-compose build nginx`
    + `docker-compose up -d nginx`
  
+ Не используйте для локальной разработки токены наших продуктовых ботов. Создайте себе своих.