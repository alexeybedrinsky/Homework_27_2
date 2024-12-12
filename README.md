
# Django Project with Docker

Этот проект использует Docker для упрощения процесса развертывания и запуска.

## Предварительные требования

- Docker
- Docker Compose

## Инструкции по запуску

1. Клонируйте репозиторий:
   ```
   git clone <URL вашего репозитория>
   cd <название_директории_проекта>
   ```

2. Создайте файл .env в корневой директории проекта и заполните его необходимыми переменными окружения (см. пример в файле .env.example).

3. Соберите и запустите контейнеры:
   ```
   docker-compose up --build
   ```

4. После успешного запуска, приложение будет доступно по адресу http://localhost:8000

5. Для выполнения миграций базы данных используйте команду:
   ```
   docker-compose exec web python manage.py migrate
   ```

6. Для создания суперпользователя выполните:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

7. Для остановки контейнеров используйте:
   ```
   docker-compose down
   ```

## Дополнительные команды

- Запуск тестов:
  ```
  docker-compose exec web python manage.py test
  ```

- Просмотр логов:
  ```
  docker-compose logs
  ```

- Доступ к shell Django:
  ```
  docker-compose exec web python manage.py shell
  ```

## Примечания

- Убедитесь, что порты 8000 и 5432 не заняты другими процессами на вашей машине.
- При внесении изменений в Dockerfile или requirements.txt, не забудьте пересобрать образы с помощью команды `docker-compose up --build`.
