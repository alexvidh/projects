from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium import webdriver
import time

@given('Нажимаю на кнопку "+" в правом верхнем углу экрана')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
        
        openButton = context.driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
        openButton.click()
time.sleep(3)

@step('Выбираю из выпадающего списка функцию "Создать новый список"')
def step_impl(context):
    selectCategory = context.driver.find_element_by_id('select2-select_category-container')
    selectCategory.click()
time.sleep(3)
    selectNewCategory = context.driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[last()]')
    selectNewCategory.click()
time.sleep(3)

@step('Нажимаю на кнопку "Отмена"')
def step_impl(context):
    cancelButton = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[1]/div')
    cancelButton.click()
time.sleep(2)

@then('Интерфейс закрывается. Открыта страница пользователя "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"')
def step_impl(context):    
    context.driver.quit()
