## Проект api_final_yatube
Проект создан в учебный целях для ищучения основ REST API с использованием Django REST framework.

### Как запустить проект в dev-режиме:
- Клонировать репозиторий (в примере используется защищенный паролем ключ SSH) и перейти в него в командной строке:
```git clone git@github.com:krtkv-alex/api_final_yatube.git```
```cd api_final_yatube```
- Cоздать и активировать виртуальное окружение:
```python3 -m venv env```
```source venv/Scripts/activate```
- Обновить pip и установить зависимости из файла requirements.txt:
```python -m pip install --upgrade pip```
```pip install -r requirements.txt```
- Выполнить миграции:
``` python manage.py migrate ```
- Запустить проект:
``` python manage.py runserver ```

### Примеры

Когда вы запустите проект, по адресу ```http://127.0.0.1:8000/redoc/``` будет доступна документация с примерами работы проекта. Документация представлена в формате Redoc.

### Автор проекта
Алексей Коротков