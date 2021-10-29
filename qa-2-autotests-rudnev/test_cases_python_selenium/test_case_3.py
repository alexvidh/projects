from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
openButton = driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
openButton.click()
time.sleep(2)

selectCategory = driver.find_element_by_id('select2-select_category-container')
selectCategory.click()
time.sleep(2)

selectNewCategory = driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[last()]')
selectNewCategory.click()
time.sleep(2)

cancelButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[1]/div')
cancelButton.click()
time.sleep(2)
driver.quit()

