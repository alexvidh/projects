Feature: Тест-кейс 3

Scenario: Запуск и закрытие интерфейса для создания новой задачи 
Given Открыта страница "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"
When Нажимаю на кнопку "+" в правом верхнем углу
And Выбираю из выпадающего списка функцию "Создать новый список"
And Нажимаю на кнопку "Отмена"
Then Интерфейс закрывается. Открыта страница пользователя "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"