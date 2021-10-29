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

@step('Ввожу данные "FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN" в поле "Заголовок"')
def step_impl(context):    

    inputProjectTitle = context.driver.find_element_by_xpath('//*[@id="project_title"]')
    inputProjectTitle.click()
    inputProjectTitle.send_keys('FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN')

@step('Ввожу данные "FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN" в поле "Название задачи"')
def step_impl(context):    

    inputProjectText = context.driver.find_element_by_xpath('//*[@id="project_text"]')
    inputProjectText.click()
    inputProjectText.send_keys('FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN')

@step('Нажимаю кнопку "ОК"')
def step_impl(context):    
okButton = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[2]')
okButton.click()

@then('Текст в новом блоке автоматически переносится на следущую строку, не пересекая границы блока')
context.driver.scroll()
context.driver.save_screenshot('text_wrapping.png')
time.sleep(10)
context.driver.quit()