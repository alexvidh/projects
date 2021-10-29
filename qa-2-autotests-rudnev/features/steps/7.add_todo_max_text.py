from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium import webdriver
import time


@given('Открыт интерфейс создания новой задачи "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"')
def step_impl(context):  
context.driver = webdriver.Chrome()
context.driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
    
    openButton = context.driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
    openButton.click()

@when('Выбираю функцию "Создать новый список"')
def step_impl(context):  
    selectCategory = context.driver.find_element_by_id('select2-select_category-container')
    selectCategory.click()

    selectNewCategory = context.driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[last()]')
    selectNewCategory.click()

@step('Ввожу данные "Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments." в поле "Заголовок"')
def step_impl(context):  
    inputProjectTitle = driver.find_element_by_xpath('//*[@id="project_title"]')
    inputProjectTitle.click()
    inputProjectTitle.send_keys('Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments.')


@step('Ввожу данные "Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments." в поле "Название задачи"') 
def step_impl(context):  
    inputProjectText = driver.find_element_by_xpath('//*[@id="project_text"]')
    inputProjectText.click()
    inputProjectText.send_keys('Change the parameter matcher used in parsing step text. The change is immediate and may be performed between step definitions in your step implementation modules - allowing adjacent steps to use different matchers if necessary. There are several parsers available in behave (by default):parse (the default, based on: parse)Provides a simple parser that replaces regular expressions for step parameters with a readable syntax like. The syntax is inspired by the Python builtin string.format() function. Step parameters must use the named fields syntax of parse in step definitions. The named fields are extracted, optionally type converted and then used as step function arguments.')


@step('Нажимаю кнопку "ОК"')
def step_impl(context):  
    okButton = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[2]')
    okButton.click()


@then('Отображается сообщение об ошибке')
def step_impl(context):  
    context.driver.save_screenshot('max_text_results.png')
    time.sleep(10)
    context.driver.quit()