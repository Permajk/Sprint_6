# Проект по автоматизации POM-тестов сервиса "Яндекс.Самокат" - Алексей Рогожников, 6 Спринт, 32 когорта

                                СОДЕРЖАНИЕ

- **tests/test_main_page.py**: тесты на странице 'https://qa-scooter.praktikum-services.ru/'.
- **tests/test_order_page.py**: тесты на странице 'https://qa-scooter.praktikum-services.ru/order'.
- **conftest.py**: фикстура для запуска тестов.
- **data.py**: тестовые данные полей ввода и url-ссылки.
- **requirements.txt**: список зависимостей, необходимых для запуска автотестов.
- **allure_results**: отчеты о выполнении тестов для дальнейшего анализа с использованием Allure.

## Запуск тестов

Чтобы запустить тесты и сгенерировать отчет, выполните следующие команды:

```bash
# Установите зависимости
pip3 install -r requirements.txt

# Запустите тесты с генерацией результата для Allure
pytest --alluredir=allure_results

# Сгенерируйте отчет Allure в виде HTML
allure serve allure_results
