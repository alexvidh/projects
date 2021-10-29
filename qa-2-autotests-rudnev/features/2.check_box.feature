Feature: Тест-кейс 2. Проверка функции чек-бокса

Scenario: Пустой чек-бокс
Given  Открыта страница "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"
When Нажимаю на чек-бокс
Then Чек-бокс отмечен, а текст задачи зачеркивается

Scenario: Отмеченный чек-бокс
Given Открыта страница "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"
When Нажимаю на чек-бокс
Then Чек-бокс пуст, а текст задачи не зачеркнут
