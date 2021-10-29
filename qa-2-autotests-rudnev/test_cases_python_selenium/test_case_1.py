from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
driver.quit()