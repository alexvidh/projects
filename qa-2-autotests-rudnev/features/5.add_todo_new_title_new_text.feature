Feature: Тест-кейс 5

Scenario: Создание новой задачи в новой категории
Given Открыт интерфейс создания новой задачи "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"
When Выбираю функцию "Создать новый список"
And Ввожу данные "Проверка" в поле "Заголовок"
And Ввожу данные "Проверка" в поле "Название задачи"
And Нажимаю кнопку "ОК"
Then В блоке с категорией "Проверка" появляется новая задача "Проверка"