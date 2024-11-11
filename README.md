# Проект по автоматизации тестирования приложения Кошелёк.ру

<br>
<p align="center">
<img width="122" title="DemoApp" src="media/logo/logo.png" alt="demoaapp">
</p>
<br>

##  📌Содержание:

- [Использованный стек технологий](#tools)
- [Реализованные проверки](#checks)
- [Требования для использование](#requirements)
- [Инструкция запуск тестов](#test_run)
- [Сборка в GitHub Action](#github-action)
- [Пример Allure-отчета](#allure_report)

<h2 id="tools">Использованный стек технологий</h2>

<p align="center">
<code><a href="https://www.python.org/"><img width="6%" title="Python" src="media/logo/python.png"></a></code>
<code><a href="https://www.jetbrains.com/pycharm/"><img width="6%" title="PyCharm IDEA" src="media/logo/PyCharm_Icon.png"></a></code>
<code><a href="https://docs.pytest.org/"><img width="6%" title="Pytest" src="media/logo/Pytest_logo.svg"></a></code>
<code><a href="https://playwright.dev/python/"><img width="6%" title="Playwright" src="media/logo/playwright-logo.png"></a></code>
<code><a href="https://allurereport.org/"><img width="6%" title="Allure Report" src="media/logo/AllureReports.png"></a></code>
<code><a href="https://github.com/"><img width="6%" title="GitHub" src="media/logo/GitHub.png"></a></code>
<code><a href="https://docs.github.com/ru/actions"><img width="6%" title="GitHub Action" src="media/logo/action.png"></a></code>
</p>



**Автотесты написаны на `Python` с использованием фреймворк `Playwright`.**
- `Pytest` - для запуска тестов.
- `Playwright` - для выполнения тестов для UI
- `GitHub Action` - CI/CD для удаленного выполнения тестов.
- `Allure Report` - для визуализация результатов теста.

**Allure-отчет включает в себя**:
* шаги выполнения тестов;
* скриншот экрана в момент подение автотеста;


 <h2 id="checks">Реализованные проверки </h2>
 
- **Негативные проверки регистрация пользователя с невалидными:**
  - [x] *Поля "Имя пользователя"*
  - [x] *Поля "Электронная почта"*
  - [x] *Поля "Пароль"*
  - [x] *Поля "Реферальный код"*

<h2 id="requirements">Требование</h2>

Клонируйте код проекта с помощью команды:
```sh
 git clone https://github.com/Mexriddin/cashru.git
```
* Установите Python версии 3.12:  https://www.python.org/downloads/

* Для создания виртуальное окружение, перейдите в директорию проекта и выполните:
```sh
 python -m venv env
```
Активация
*  Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:
```sh
 venv\Scripts\activate.bat - для Windows
 ```
```sh
 source venv/bin/activate - для Linux и MacOS
``` 
Установка зависимости
*  Чтобы установить зависимости проекта в виртуальное окружение, необходимо выполнить:
```sh
 pip install -r .\requirements.txt
 ```
```sh
 playwright install
 ```


<h2 id="test_run">Инструкция запуск тестов</h2>
Запуск тестов можно осуществлять локально или с помощью <a href="https://github.com/Mexriddin/cashru/actions/workflows/ci.yml"> GitHub Actions</a> с формированием Allure-отчета прогона.

**С возможностью выбора окружение и браузер**
### Локальный запуск тестов

* в .env определить параметры конфигурации:

    - `STAGE`*(prod,dev)*

```sh
  pytest .\tests\ 
```
При необходимости можно переопределить параметры запуска
```
pytest --browser=chromium           - запуск с выбором в каком браузере(chromium, firefox, webkit)
pytest -n=4                         - запуск параллельно в 4 потоках
pytest -v                           - запуск с дополнительным информациям
pytest --alluredir=allure-results   - c генирированием Allure отчета
```
### Запуск тестов с помощью Docker
Запускаем тесты в докер контейнере
```sh
docker-compose up run_tests
```
Генирируем Allure отчет
```sh
docker-compose up report
```

<h2 id="github-action"><img width="3%" title="GitHub Action" src="media/logo/action.png"> <a href="https://github.com/Mexriddin/cashru/actions/workflows/ci.yml"> Сборка в GitHub Action</a></h2>
<h4>С возможностью выбора окружение и браузер</h4>
<p align="center">
<img title="GitHub Action" src="media/screens/github_actions.png">
</p>

<h2 id="allure_report"><img width="3%" title="Allure Report" src="media/logo/AllureReports.png"> <a href="https://mexriddin.github.io/cashru/">Пример Allure-отчета</a></h2>
<h4>Обзор</h4>

<p align="center">
<img title="Allure Overview" src="media/screens/allure_report_dash.png">
</p>

### Результат выполнения теста

<p align="center">
<img title="Test Results in Alure" src="media/screens/allure_report_result.png">
</p>
