# Установка и запуск
1. Скопировать `.env.example` в `.env`
2. Добавить ключ приложения  `SECRET_KEY=` в `.env`
3. Запустить `docker-compose`
```bash
docker-compose up -d
```

Postgresql:
- user: `postgres`
- password: `fghjkl5678`
- host_port: `localhost:5432`

PgAdmin:
- user: `admin@admin.ru`
- password: `password`
- host_port: `http://localhost:5050/`

# Остановка сервисов
```bash
docker-compose stop
```
