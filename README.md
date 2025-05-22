# Django Tree Menu App

Это тестовое задание на реализацию древовидного меню в Django.

## 📌 Условия задачи

- Меню реализовано через template tag
- Все пункты над активным пунктом раскрыты
- Первый уровень вложенности под активным пунктом раскрыт
- Данные хранятся в БД
- Меню редактируется в стандартной админке Django
- Активный пункт определяется по текущему URL
- Меню на одной странице может быть несколько (по имени)
- URL может быть как явным, так и именованным
- На отрисовку одного меню — **ровно один запрос к БД**
- Используется только Django и стандартная библиотека Python

## 🚀 Установка и запуск

1. Клонируйте проект:

```bash
git clone https://github.com/yourusername/django-tree-menu.git
cd django-tree-menu


python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
pip install -r requirements.txt


python manage.py migrate

python manage.py createsuperuser

Перейдите в админку: http://127.0.0.1:8000/admin

Подключите тег и отобразите меню:


{% load menu_tags %}
{% draw_menu 'main_menu' %}

    О сайте (/about/)

        Команда (/about/team/)

    Контакты (/contacts/)

    Услуги (/services/)



