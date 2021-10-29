from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
checkbox = driver.find_element_by_id('todo_check')
checkbox.click()
driver.save_screenshot('checkbox_results_1.png')
time.sleep(2)

checkbox = driver.find_element_by_id('todo_check')
checkbox.click()
driver.save_screenshot('checkbox_results_2.png')
driver.quit()

pass