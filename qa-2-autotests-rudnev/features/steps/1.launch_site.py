from behave import given, then  # pylint: disable=no-name-in-module
from selenium import webdriver


@given('я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')


@then('открылась страница с Задачами')
def step_impl(context):
    text = context.driver.find_element_by_xpath('<h1 class="title">Задачи</h1>').text
    assert text == "Задачи"
