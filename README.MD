В рамках самообучения по  Python и Selenium тренировался в написании автотестов.
Проект представляет собой ряд тестов на различный функционал вебстраницы.

Использовал pytest и Selenium Webdriver. Дополнительно подключал библиотеку requests.

Реализован Page Object.
Также в отдельные модули вынесены  тестовые данные, локаторы и контент.

При запуске можно указать в каком браузере будут запущены тесты Chrome или Firefox(по умолчанию Chrome)

test_checkboxes - тестирование чекбоксов

test_form_authentication - тестирование формы авторизации

test_javascript_alerts - тестирование алертов

test_status_code - тестирование кода ответа

Для запуска  скачать проект, установить все зависимости из requirements.txt.
На машине должен быть установлен chromedriver
https://sites.google.com/chromium.org/driver/ - скачать можно отсюда для вашей версии браузера.


В терминале запуск командой: pytest Tests/
Для запуска в firefox: pytest --browser_name "firefox" Tests/
