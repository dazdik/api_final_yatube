# api_final
api final
### Проект «API для Yatube»

### Описание
API для проекта Yatube.

### Функционал
- Реализован REST API для сервиса Yatube;
- Для аутентификации использованы JWT-токены;
- Работает со всеми моделями Yatube: постами, комментариями, группами и подписками;
- Поддерживает методы GET, POST, PUT, PATCH, DELETE;
- Предоставляет данные в формате JSON.

### Запуск проекта в dev-режиме
1. Клонировать репозиторий: 
```
git clone https://github.com/dazdik/api_final_yatube.git
```
2. Перейти в папку с проектом.
```
cd api_final_yatube
```

3. Установить виртуальное окружение:
```
python -m venv venv
``` 
4. Активировать виртуальное окружение:
```
# для OS Lunix и MacOS
source venv/bin/activate
# для OS Windows
source venv/Scripts/activate
```
5. Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
6. Выполнить миграции на уровне проекта:
```
cd yatube_api
python manage.py migrate
````
7. Запустить проект на локальном сервере:
```
python manage.py runserver
# адрес запущенного проекта
http://127.0.0.1:8000
```

### Документация для API с примерами запросов
```
http://127.0.0.1:8000/redoc/
```
