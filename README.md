# Тестовое задание

### Стек

- Python
- Docker

### Фреймворки и Библиотеки

- aiogram - фреймворк для TelegramBotAPI
- aiohttp - для отправки запровс в API для получения курса валют

***

### Настройка и создание файла конфигурации

Все файлы настроек хранятся по умолчанию в директории __/config__.
Файл __config-example.yml__ - пример конфигурационного файлы

bot.token - Токен бота, создается с помощью [BotFather](https://t.me/BotFather)

bot.admin_id - telegram_id владельца бота, не обьязателен к заполнению

db.host - хост для postgres, должен совпадать с данными из docker-compose.yml

db.database - БД для postgres, должен совпадать с данными из docker-compose.yml

db.user и db.password - имя пользователя и пароль для postgres, должен совпадать с данными из docker-compose.yml

logging.level - уровень логирования

***

### Создание и запус бота через Docker

```
docker build . -t bot
docker-compose up
```

***

### Локальный запуск

Создание виртуального окружения и установка зависимостей

```
python3 -m venv venv
pip install -r requirements.txt
```

Запуск бота осуществляется через команду

```
python3 app.py
```
