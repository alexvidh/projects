from behave import given, when, then, step  # pylint: disable=no-name-in-module
from selenium import webdriver
import time

@given('Открыт интерфейс создания новой задачи "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"')
def step_impl(context):    
    context.driver = webdriver.Chrome()
    context.driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
        
        openButton = context.driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
        openButton.click()

@when('Выбираю категорию "Семья"')
def step_impl(context):
    selectCategory = context.driver.find_element_by_id('select2-select_category-container')
    selectCategory.click()
        
        selectFamilyCategory = context.driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[1]')
        selectFamilyCategory.click()

@step('Ввожу данные "Покормить кота" в поле "Название задачи"')
def step_impl(context):    
    inputProjectText = context.driver.find_element_by_xpath('//*[@id="project_text"]')
    inputProjectText.click()
    inputProjectText.clear('Покормить кота')


@step('Нажимаю кнопку "ОК"')
def step_impl(context):
    okButton = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[2]')
    okButton.click()


@then('В блоке с категорией "Семья" появляется новая задача "Покормить кота"')
def step_impl(context):
    context.driver.save_screenshot('new_todo_text.png')
    context.driver.quit()