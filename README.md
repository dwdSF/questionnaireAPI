# questionnaireAPI
API для системы опросов пользователей.


## Инструкция по запуску
  - Склонировать репозиторий к себе на компьютер
  - Установить виртуальное окружение и активировать
```shell
python3 -m venv env
env\bin\activate
```
  - Установить зависимости
```shell
pip3 install -r requirements.txt
```
  - Создать и предварительно заполнить базу данных
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
  - Запуск web-приложения
```python3 manage.py runserver```

# Документация к API доступна после запуска локально по адресу: http://127.0.0.1:8000/redoc/
