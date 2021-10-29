from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://qa-assignment.oblakogroup.ru/board/aleksandr_rudnev')
openButton = driver.find_element_by_xpath('//*[@id="add_new_todo"]/img')
openButton.click()

selectCategory = driver.find_element_by_id('select2-select_category-container')
selectCategory.click()

selectNewCategory = driver.find_element_by_xpath('/html[1]/body[1]/span[1]/span[1]/span[2]/ul[1]/li[last()]')
selectNewCategory.click()

inputProjectTitle = driver.find_element_by_xpath('//*[@id="project_title"]')
inputProjectTitle.click()
inputProjectTitle.send_keys('Проверка')

inputProjectText = driver.find_element_by_xpath('//*[@id="project_text"]')
inputProjectText.click()
inputProjectText.send_keys('Проверка')

okButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/form/a[2]')
okButton.click()
driver.quit()
