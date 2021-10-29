Feature: Тест-кейс 7

Scenario: Создание новой задачи с количеством знаков больше максимального
Given Открыт интерфейс создания новой задачи "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"
When Выбираю функцию "Создать новый список"
And Ввожу данные "Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments." в поле "Заголовок" 
And Ввожу данные "Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments." в поле "Название задачи" 
And Нажимаю кнопку "ОК"
Then Отображается сообщение об ошибке
