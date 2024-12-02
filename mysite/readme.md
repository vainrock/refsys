# Referral System API

Это простая реферальная система, реализованная на Python, Django и PostgreSQL. Система позволяет пользователям регистрироваться, используя свои номера телефонов, генерировать коды приглашений и отслеживать рефералов.

## Характеристики
- Авторизация пользователя по номеру телефона с 4-значным OTP.
- Уникальные 6-символьные коды приглашения, генерируемые для каждого пользователя при первой регистрации.
- Возможность активировать реферальный код в профиле пользователя.
- Отображение пользователей, использовавших пригласительный код текущего пользователя.

## Используемые технологии
- **Стек**: Python, Django, Django REST Framework (DRF)
- **База данных**: PostgreSQL
- **Способ размещения**: [PythonAnywhere](https://www.niki.pythonanywhere.com, но сайт пока не работает)

## Инструкции по установке
### Необходимые условия
- Python 3.10 или выше
- Установленный и запущенный PostgreSQL
- Django, DRF

### Установка

1. Клонируйте репозиторий:
    ``bash
    git clone <repository_url>
    cd referral_system
    ```

2. Создайте и активируйте виртуальную среду:
    ``bash
    python -m venv env
    source env/bin/activate # Linux/MacOS
    env\Scripts\activate # Windows
    ```

3. Установите зависимости:
    ``bash
    pip install -r requirements.txt
    ```

4. Настройте базу данных PostgreSQL:
    - Обновите параметр `DATABASES` в `settings.py`, указав свои учетные данные PostgreSQL.

5. Примените миграции:
    ``bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Запустите сервер разработки:
    ``bash
    python manage.py runserver
    ```

### Конечные точки API
#### 1. **Авторизация пользователя**
- **Конечная точка**: `/api/authorize/`
- **Метод**: `POST`
- **Тело запроса**:
  ``json
  {
    «phone_number": «1234567890»
  }