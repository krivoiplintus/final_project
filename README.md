# final_project
Дипломная работа в SkyPro по специальности QA

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/krivoiplintus/final_project.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- allure
- configparser
- json

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./configyration - провайдер настроек
  - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
  - test_data.json - тестовые данные

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [base_url](https://www.chitai-gorod.ru/)