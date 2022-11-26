![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

### Социальная сеть Yatube (Учебный проект)

## Описание
Социальная сеть с дневниками, сообществами и...

## Технологии
Python 3.7 Django 2.2.19

## **Запуск проекта**

- Клонировать репозиторий:
 ```  git clone https://github.com/Semyonov-K/infra_sp2.git  ```

- Создать .env файл в директории /infra/

- Вставить в .env файл следующие переменные:
 ```  DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql  ```
 ```  DB_NAME=postgres # имя базы данных  ```
 ```  POSTGRES_USER=postgres # логин для подключения к базе данных ```
 ```  POSTGRES_PASSWORD= # установите свой пароль для подключения к БД ```
 ```  DB_HOST=db # название сервиса (контейнера) ```
 ```  DB_PORT= # укажите порт для подключения к БД ```

- Перейти в папку infra и запустить сборку контейнеров при помощи докера:
 ```  cd infra_sp2/infra ```
 ```  docker-compose up ```

- Для пересборки контейнеров выполнять команду: (находясь в папке infra, при запущенном Docker):
 ```  docker-compose up -d --build ```

- В контейнере web выполнить миграции:
 ```  docker-compose exec web python manage.py migrate --run-syncdb ```
 ```  docker-compose exec web python manage.py migrate ```

- Создать суперпользователя:
 ```  docker-compose exec web python manage.py createsuperuser ```

- Собрать статику:
 ```  docker-compose exec web python manage.py collectstatic --no-input ```

- Проверьте работоспособность приложения, для этого перейдите на страницу:
 ``` http://localhost/admin/ ```

- Для заполнения базы данных выполните последовательно следующие команды:
 ```  python3 manage.py shell  ```  
# выполнить в открывшемся терминале:
 ```  >>> from django.contrib.contenttypes.models import ContentType  ```
 ```  >>> ContentType.objects.all().delete()  ```
 ```  >>> quit()  ```

 ```  python manage.py loaddata dump.json  ```
- Проект готов к работе
- Автор: Кирилл 