# Recipe API

API для управления рецептами, категориями, ингредиентами и отзывами. Разработано на Django REST Framework.

## Стек

- Django 5
- Django REST Framework
- drf-spectacular (Swagger UI)
- MS SQL Server

## Запуск

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/

Админка: http://127.0.0.1:8000/admin/

## Структура проекта

```
recipe_api/
├── manage.py
├── requirements.txt
├── recipe_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api_v1/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── permissions.py
    ├── admin.py
    └── migrations/
```

## Эндпоинты

### Категории

| Метод | URL | Описание |
|---|---|---|
| GET | /api/v1/categories/ | Список категорий |
| GET | /api/v1/categories/{id}/ | Одна категория |
| POST | /api/v1/categories/ | Создать одну или несколько |
| PUT | /api/v1/categories/{id}/ | Полное обновление |
| PATCH | /api/v1/categories/{id}/ | Частичное обновление |
| DELETE | /api/v1/categories/{id}/ | Удалить одну или несколько (?ids=1,2,3) |

Фильтры: ?name=

### Ингредиенты

| Метод | URL | Описание |
|---|---|---|
| GET | /api/v1/ingredients/ | Список ингредиентов |
| GET | /api/v1/ingredients/{id}/ | Один ингредиент |
| POST | /api/v1/ingredients/ | Создать один или несколько |
| PUT | /api/v1/ingredients/{id}/ | Полное обновление |
| PATCH | /api/v1/ingredients/{id}/ | Частичное обновление |
| DELETE | /api/v1/ingredients/{id}/ | Удалить один или несколько (?ids=1,2,3) |

Фильтры: ?name=, ?unit=

### Рецепты

| Метод | URL | Описание |
|---|---|---|
| GET | /api/v1/recipes/ | Список рецептов |
| GET | /api/v1/recipes/{id}/ | Один рецепт |
| POST | /api/v1/recipes/ | Создать один или несколько |
| PUT | /api/v1/recipes/{id}/ | Полное обновление |
| PATCH | /api/v1/recipes/{id}/ | Частичное обновление |
| DELETE | /api/v1/recipes/{id}/ | Удалить один или несколько (?ids=1,2,3) |

Фильтры: ?title=, ?category_id=, ?difficulty=, ?ingredient_id=

### Отзывы

| Метод | URL | Описание |
|---|---|---|
| GET | /api/v1/reviews/ | Список отзывов |
| GET | /api/v1/reviews/{id}/ | Один отзыв |
| POST | /api/v1/reviews/ | Создать один или несколько |
| PUT | /api/v1/reviews/{id}/ | Полное обновление |
| PATCH | /api/v1/reviews/{id}/ | Частичное обновление |
| DELETE | /api/v1/reviews/{id}/ | Удалить один или несколько (?ids=1,2,3) |

Фильтры: ?recipe_id=, ?rating=

## Примеры запросов

Создать категорию:
```json
{"name": "Супы", "description": "Горячие первые блюда"}
```

Создать несколько категорий:
```json
[{"name": "Десерты"}, {"name": "Салаты"}]
```

Создать рецепт:
```json
{
    "title": "Картофельный суп",
    "instructions": "Нарезать, варить 20 минут, посолить",
    "cook_time_min": 30,
    "servings": 4,
    "difficulty": "easy",
    "category_id": 1,
    "ingredient_ids": [1, 2, 3]
}
```

Создать отзыв:
```json
{"recipe_id": 1, "text": "Очень вкусно!", "rating": 5}
```
