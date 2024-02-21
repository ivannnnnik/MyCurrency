# MyCurrency

## Документация API

**Документация API сервиса будет доcтупна после его запуска, по адресу:**

- http://127.0.0.1/swagger/

**Формат вставки токена при авторизации интерфейса Swagger:** *Bearer <your_token>*

## Инструкция по запуску

1. Поднять контейнеры

```commandline
sudo docker-compose up -d 
```

2. Применить миграции

```commandline
sudo docker-compose exec backend python manage.py migrate
```

3. Загрузить данные курсов валют

```commandline
sudo docker-compose exec backend python manage.py update_currency
```

4. Собрать статику

```commandline
sudo docker-compose exec backend python manage.py collectstatic
```

5. Скопировать статику

```commandline
sudo docker-compose exec backend cp -r /app/static/. /static/static/
```

6. Запуск тестов

```commandline
sudo docker-compose exec backend coverage run manage.py test 
```

7. Покрытие тестами

```commandline
sudo docker-compose exec backend coverage report

```

8. Создание суперпользователя

```commandline
sudo docker-compose exec backend python manage.py createsuperuser

```
