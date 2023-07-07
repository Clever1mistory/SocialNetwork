
# FastAPI приложение SocialNetwork

Данное FastAPI приложение представляет собой простую социальную сеть с возможностью авторизации, добавления, редактирования, удаления и лайка постов, а также встроенный чат на вебсокетах.

## Установка и запуск

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Склонируйте репозиторий:

git clone git@github.com:Clever1mistory/SocialNetwork.git

3. Установите зависимости из файла requirements.txt:

pip install -r requirements.txt

4. Запустите приложение: <ins>Перед запуском убедитесь, что src помечена как source root</ins>

uvicorn src.main:app --reload

Приложение будет доступно по адресу http://localhost:8000.

## API документация

API документация доступна по адресу [http://localhost:8000/docs](http://localhost:8000/docs). Здесь вы можете ознакомиться со всеми доступными эндпоинтами, их параметрами и ожидаемыми ответами.

## Фронтенд

Для удобного взаимодействия с приложением был создан небольшой фронтенд с использованием fastapi.templating. Шаблоны находятся в папке templates. Для запуска фронтенда откройте веб-браузер и перейдите по адресу [http://localhost:8000/pages/base](http://localhost:8000/pages/base).

## Стек

- Python 3.11
- FastAPI
- WebSocket
- SQLAlchemy
- requirements.txt


## Авторы

- Clever1mistory
- clever1mistory@gmail.com
