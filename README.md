# Тестовое задание на Python Dev
<hr>

### #1. FastAPI + Redis

**Запуск проекта:**
1. `git clone`
2. `cp .envExample .env`
3. `docker compose -f docker-compose.dev.yaml up --build`


**Запросы:**
1. Запись/Обновление
```
curl -X 'PUT' \
  'http://localhost:8000/write_data/' \
  -H 'Content-Type: application/json' \
  -d '{
  "phone": "88005553535",
  "address": "ул. Ленина, д. 1, кв. 5"
}'
```

2. Получение

```
curl -X 'GET' 'http://localhost:8000/check_data?phone=88005553535'
```

### #2. СУБД PostgreSQL
