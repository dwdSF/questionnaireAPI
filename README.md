# questionnaireAPI
API для системы опросов пользователей.


## Инструкция по запуску
  - Склонировать репозиторий к себе на компьютер
  - Установить виртуальное окружение и активировать
```shell
python3 -m venv env
source env\bin\activate
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
```
python3 manage.py runserver
```

#### Документация к API доступна после запуска локально по адресу: http://127.0.0.1:8000/redoc/  
  
  
## Возможная проблема при получении токена
```shell
AttributeError: 'str' object has no attribute 'decode'
```
Ошибка связана с попыткой декодировать объект, который уже декодирован.  
А начиная с Python 3, вся строка уже является объектом unicode.  
#### **Фикс**:
1. Установить виртуальное окружение
2. Установить зависимости
3. Перейти ```questionnaireAPI\env\lib\site-packages\rest_framework_simplejwt\backends.py```
4. В функции ```encode``` изменить ```return token.decode('utf-8')``` на ```return token```
