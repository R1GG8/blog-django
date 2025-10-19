Django-проект с приложениями `blog`, `users` и `main`.

## Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/username/mysite.git
cd mysite
```
2. Создать виртуально окружение: 

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Установить зависимости:

pip install -r requirements.txt

4. Создать файл .env с настройками:

SECRET_KEY=your_secret_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

5. Применить миграции:

python manage.py migrate

6. Создать суперпользователя:

python manage.py createsuperuser

7. Запустить сервер: 

python manage.py runserver
