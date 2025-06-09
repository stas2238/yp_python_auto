## Описание
Автоматизированные тесты для проверки функциональности регистрации, логина, логаута и создания объявлений на сервисе qa-desk (https://qa-desk.stand.praktikum-services.ru/).

## Запуск тестов
1. Установите зависимости:
   pip3 install selenium
для Mac:
1.1. Подготовьте virtual env, затем установите зависимости из шага 1:
    python3 -m venv path/to/venv
    source path/to/venv/bin/activate

## Структура проекта
- tests/ — тесты
- locators/ — локаторы
- conftest.py — фикстуры
- utils.py — вспомогательные функции