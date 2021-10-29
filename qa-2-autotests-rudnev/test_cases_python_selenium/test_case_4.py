from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
openButton = driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
openButton.click()

selectCategory = driver.find_element_by_id('select2-select_category-container')
selectCategory.click()

selectFamilyCategory = driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[1]')
selectFamilyCategory.click()

inputProjectText = driver.find_element_by_xpath('//*[@id="project_text"]')
inputProjectText.click()
inputProjectText.send_keys('Покормить кота')

okButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[2]')
okButton.click()

driver.save_screenshot('new_todo_text.png')
driver.quit()
