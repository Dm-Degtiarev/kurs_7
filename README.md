# Курсовая работа №7

Приложение является backend частью приложения напоминания о привычках, которые необходимо производить по времени. Оповещения о которых приходят в telegram.

# Запуск
1. Установить зависимости: pip install -r requirements.txt
2. Устапновить Redis
3. Запустить сервер: python manage.py runserver
4. Создать супер потзователя: python manage.py csu (уч. данные смотреть в файле csu)
5. Зарегистрировать пользователей. Регистрация доступна через API. Более детально описано в swagger / redoc
6. Настроить привычки (REST запросами или через админку)
7. Создать .env куда поместить необходимые данные. См. шаблон .env.sample
8. Заупустить Celery: celery -A config worker -l INFO -P eventlet
9. Заупустить celery-beat: celery -A config beat -l INFO

Важно! Обязательно необходимо узнать свой ID-юзер в Telegram и записать его в модель User.
Узнать ID можно через бота @userinfobot
На данный момент все пользователям я присвоил свой ID и никнейм. Необходимо заменить на свои данные.

Привычки уже заведены в БД, при необходимости можно дополнить список. 

# Docker
Для windows необходимо установить desktop версию Docker.
Для Linux: https://docs.docker.com/engine/install/ - выбираем необходимую ОС

После успешной утсановки необходимо выполнить команду: docker-compose up --build

# Документация
api/redoc или api/swagger

   
