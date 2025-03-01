# Teleport

## Hруководство для запуска тестов проекта Teleport

### Шаги
1. Склонировать проект 'git clone https://github.com/KliuevDmitrii/Teleport.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- _selenium_
- requests
- _sqlalchemy_
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- test_config.ini - настройки для тестов

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)


### Библиотеки
- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests