<h1 align="centre"> Автоматизированные UI и API тесты AR Mobile</h1>

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Selene](https://img.shields.io/badge/selene-2.0.0rc9-green.svg)
![Allure](https://img.shields.io/badge/allure-2.15.0-orange.svg)
![Pytest](https://img.shields.io/badge/pytest-8.4.1-yellow.svg)

## 📌 О проекте

Автоматизированные тесты для веб-интерфейса и API приложения для строительного контроля, покрывающие:
- Авторизацию пользователей по ролям (Владелец, Администратор, Инспектор, Подрядчик, Наблюдатель, Супервизор)
- Работу с проектом (создание и удаление проекта, поиск по проектам, завершение проекта)
- Проверку недоступности создания, удаления и завершения проекта под ролями (Администратор, Инспектор, Подрядчик, Наблюдатель, Супервизор)

## 🛠 Технологический стек

- **Python** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Selene** - удобная обертка над Selenium
- **Pytest** - фреймворк для тестирования
- **Allure** - генератор отчетов
- **Allure TestOps** - генерация тестовой документации
- **Jenkins** - система непрерывной интеграции
- **Selenoid** - контейнеризованный запуск браузеров

## 🌐 CI/CD и Мониторинг

### <img src="https://jenkins.io/images/logos/jenkins/jenkins.svg" width="20"> **Jenkins Pipeline**

**Ссылка на сборку**:  
[**AR Mobile Job**](https://jenkins.autotests.cloud/job/LuckyDucky_qa_guru_python_armobile/)

**Особенности пайплайна**:
- Запуск тестов с использованием браузера в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram
- Генерация тестовой документации в Allure TestOps

### <img src="https://arm.vr-arsoft.com/faviconARM.ico" width="20"> AR Mobile  
**Пример прохождения тестов**  
![Test image](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0.png)   
![Test video](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%20gif.gif)

### <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="20"> Allure Report
**Пример отчёта**:  
[**AR Mobile Report**](https://jenkins.autotests.cloud/job/LuckyDucky_qa_guru_python_armobile/allure/)

![Report image](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/chrome_GUyHfwyTQv.png)  
![Report image2](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/chrome_JSGA2eXQ1e.png)

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Пример отчета от telegram бота**:  
![Telegram bot image](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/Telegram_KS4BvFfjMH.png)

### <img src="https://allure.autotests.cloud/favicon.ico" width="20"> Allure TestOps
**Пример тестовой документации**:  
![Allure TestOps image](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/chrome_h2e5AtNo6Q.png)
![Allure TestOps image2](https://github.com/LuckyDuckyGGG/ARM_project/blob/main/resources/chrome_h0D2vqMBNO.png)