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
<hr>

### #2. СУБД PostgreSQL

**Способ 1 (1 запрос):**

```
UPDATE full_names
SET status = s.status
FROM short_names s
WHERE full_names.name LIKE s.name || '%';
```


**Способ 2 (3 запроса):**

1. Создание временной таблицы без расширений
```
CREATE TEMP TABLE temp_full_names AS
SELECT 
  REGEXP_REPLACE(name, '\..*$', '') AS name_without_extension,
  name,
  status
FROM full_names;
```

2. Перенос данных из временной таблицы

```
UPDATE full_names
SET status = s.status
FROM short_names s
JOIN temp_full_names t ON s.name = t.name_without_extension
WHERE full_names.name = t.name;
```

3. Удаление временной таблицы

```
DROP TABLE temp_full_names;
```


**Способ 3 (1 запрос):**

```
WITH updated_names AS (
  SELECT 
    fn.name AS full_name, 
    sn.status AS new_status
  FROM 
    full_names fn
  JOIN 
    short_names sn 
  ON 
    sn.name = REGEXP_REPLACE(fn.name, '\..+$', '')
)
UPDATE full_names
SET status = updated_names.new_status
FROM updated_names
WHERE full_names.name = updated_names.full_name;
```