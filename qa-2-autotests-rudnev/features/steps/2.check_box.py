from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium import webdriver
import time

@given('Открыта страница "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"') 
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')

@when('Нажимаю на чек-бокс')
def step_impl(context)
    checkbox = context.driver.find_element_by_id('todo_check')
    checkbox.click()
time.sleep(2)

@then('Чек-бокс отмечен, а текст задачи зачеркивается')
def step_impl(context)
    context.driver.save_screenshot('checkbox_results_1.png')

@then('Чек-бокс пуст, а текст задачи не зачеркнут')
def step_impl(context)
    context.driver.save_screenshot('checkbox_results_2.png')
    context.driver.quit()